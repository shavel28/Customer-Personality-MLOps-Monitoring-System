from flask import Flask, request, jsonify
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import requests
import time

app = Flask(__name__)

MODEL_URL = "http://localhost:5000/invocations"

REQUEST_TOTAL = Counter("ml_requests_total", "Total request aktual ke endpoint inferensi")
REQUEST_SUCCESS = Counter("ml_requests_success_total", "Total request inferensi yang berhasil")
REQUEST_FAILED = Counter("ml_requests_failed_total", "Total request inferensi yang gagal")
INFERENCE_COUNT = Counter("ml_inference_count_total", "Total inferensi aktual yang dieksekusi")

LATENCY = Histogram("ml_prediction_latency_seconds", "Latency aktual proses inferensi model")
LAST_STATUS = Gauge("ml_last_status_code", "Status code terakhir dari model serving")
LAST_PREDICTION = Gauge("ml_last_prediction", "Hasil prediksi terakhir dari model")
MODEL_UP = Gauge("ml_model_up", "Status ketersediaan model, 1 aktif dan 0 mati")
INPUT_ROWS = Gauge("ml_input_rows", "Jumlah baris input pada request terakhir")
RESPONSE_TIME = Gauge("ml_response_time", "Response time aktual request terakhir")

@app.route("/")
def home():
    return jsonify({
        "service": "Real ML Monitoring Exporter",
        "status": "running",
        "metrics": "/metrics",
        "predict": "/predict"
    })

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()

    REQUEST_TOTAL.inc()

    rows = payload.get("dataframe_split", {}).get("data", [])
    INPUT_ROWS.set(len(rows))

    start_time = time.time()

    try:
        response = requests.post(
            MODEL_URL,
            json=payload,
            timeout=15
        )

        latency = time.time() - start_time

        LATENCY.observe(latency)
        RESPONSE_TIME.set(latency)
        LAST_STATUS.set(response.status_code)

        if response.status_code == 200:
            REQUEST_SUCCESS.inc()
            INFERENCE_COUNT.inc()
            MODEL_UP.set(1)

            result = response.json()
            prediction = result["predictions"][0]
            LAST_PREDICTION.set(float(prediction))

            return jsonify({
                "status": "success",
                "source": "actual_model_inference",
                "model_url": MODEL_URL,
                "latency_seconds": latency,
                "model_response": result
            }), 200

        REQUEST_FAILED.inc()
        MODEL_UP.set(0)

        return jsonify({
            "status": "failed",
            "source": "actual_model_inference",
            "model_status_code": response.status_code,
            "model_response": response.text
        }), 500

    except Exception as error:
        latency = time.time() - start_time

        REQUEST_FAILED.inc()
        MODEL_UP.set(0)
        LAST_STATUS.set(0)
        RESPONSE_TIME.set(latency)

        return jsonify({
            "status": "error",
            "source": "actual_model_inference",
            "error": str(error)
        }), 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    print("Real monitoring exporter berjalan di http://localhost:8000")
    print("Endpoint inference aktual: http://localhost:8000/predict")
    print("Endpoint metrics: http://localhost:8000/metrics")
    app.run(host="0.0.0.0", port=8000)