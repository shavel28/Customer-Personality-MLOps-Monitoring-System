import requests

# =========================================================

# REAL INFERENCE REQUEST

# Mengirim request inferensi aktual ke model yang berjalan

# melalui Prometheus Exporter -> MLflow Docker Model

# =========================================================

url = "http://localhost:8000/predict"

payload = {
"dataframe_split": {
"columns": [
"Year_Birth",
"Income",
"Kidhome",
"Teenhome",
"Recency",
"MntWines",
"MntFruits",
"MntMeatProducts",
"MntFishProducts",
"MntSweetProducts",
"MntGoldProds",
"NumDealsPurchases",
"NumWebPurchases",
"NumCatalogPurchases",
"NumStorePurchases",
"NumWebVisitsMonth",
"AcceptedCmp3",
"AcceptedCmp4",
"AcceptedCmp5",
"AcceptedCmp1",
"AcceptedCmp2",
"Complain",
"Z_CostContact",
"Z_Revenue",
"Response",
"TotalSpending",
"Education_Basic",
"Education_Graduation",
"Education_Master",
"Education_PhD",
"Marital_Status_Alone",
"Marital_Status_Divorced",
"Marital_Status_Married",
"Marital_Status_Single",
"Marital_Status_Together",
"Marital_Status_Widow",
"Marital_Status_YOLO"
],
"data": [[
1985,
50000,
1,
0,
10,
100,
20,
50,
10,
5,
10,
2,
3,
1,
4,
5,
0,
0,
0,
0,
0,
0,
3,
11,
0,
195,
0,
1,
0,
0,
0,
0,
1,
0,
0,
0,
0
]]
}
}

response = requests.post(
url,
json=payload
)

print("STATUS :", response.status_code)
print("RESULT :", response.text)
