# Customer Personality MLOps Monitoring System

## Overview

Customer Personality MLOps Monitoring System is an end-to-end Machine Learning Operations (MLOps) project that demonstrates the complete machine learning lifecycle, from experiment tracking and model development to deployment, monitoring, logging, and alerting.

The project utilizes the Customer Personality Analysis dataset and implements industry-standard MLOps tools such as MLflow, DagsHub, Docker, GitHub Actions, Prometheus, and Grafana to build a production-oriented machine learning workflow.

This repository showcases how machine learning models can be developed, managed, deployed, monitored, and maintained effectively using modern MLOps practices.

---

## Project Objectives

* Develop a machine learning model for customer personality analysis.
* Track experiments, parameters, metrics, and artifacts using MLflow.
* Store and manage model artifacts using DagsHub.
* Automate workflows using GitHub Actions.
* Deploy machine learning models using Docker and MLflow Model Serving.
* Monitor deployed services using Prometheus.
* Visualize operational metrics using Grafana dashboards.
* Configure alerting mechanisms for monitoring critical conditions.

---

## Dataset

### Customer Personality Analysis Dataset

This project uses the Customer Personality Analysis Dataset obtained from Kaggle.

Dataset Source:

https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

### Dataset Features

The dataset contains customer demographic and purchasing behavior information, including:

* Customer Income
* Family Structure
* Recency
* Product Spending
* Purchase Frequency
* Campaign Responses
* Web Purchases
* Store Purchases
* Customer Engagement Information

The dataset is used to support customer personality prediction and behavioral analysis.

---

## Project Stages

### 1. Experiment Tracking

This stage focuses on machine learning experimentation and experiment management.

#### Activities

* Data Exploration
* Data Preprocessing
* Feature Engineering
* Model Experimentation
* Parameter Tracking
* Metrics Logging
* Artifact Logging

#### Tools

* MLflow
* Python
* Scikit-Learn

#### Outputs

* Experiment Runs
* Logged Parameters
* Logged Metrics
* Model Artifacts

---

### 2. Machine Learning Model Development

This stage focuses on developing and evaluating machine learning models.

#### Activities

* Data Cleaning
* Data Transformation
* Feature Engineering
* Model Training
* Model Evaluation
* Model Selection

#### Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn

#### Outputs

* Trained Machine Learning Model
* Evaluation Results
* Model Artifact (.pkl)

---

### 3. CI/CD Workflow and Deployment

This stage implements deployment automation and workflow integration.

#### Activities

* Version Control Management
* Continuous Integration
* Continuous Deployment
* Docker Containerization
* MLflow Model Serving

#### Technologies

* GitHub
* GitHub Actions
* Docker
* MLflow

#### Outputs

* Automated Workflow Pipeline
* Docker Image
* Running Model Service
* Deployment Environment

---

### 4. Monitoring and Logging

This stage focuses on monitoring machine learning services after deployment.

#### Technologies

* Prometheus
* Grafana

#### Monitoring Metrics

##### Request Metrics

* Total Prediction Requests
* Successful Prediction Requests
* Failed Prediction Requests
* Total Inference Executed

##### Model Metrics

* Last Prediction Result
* Model Availability Status
* Input Rows Processed

##### Performance Metrics

* Prediction Latency
* Response Time
* Response Status Code

#### Outputs

* Monitoring Dashboard
* Metrics Collection System
* Logging System
* Alert Rules
* Alert Notifications

---

## Alerting Configuration

The monitoring system includes alerting rules for identifying service disruptions and performance issues.

### Model Down Alert

Triggered when:

```text
ml_model_up < 1
```

### Prediction Failed Alert

Triggered when:

```text
ml_requests_failed_total > 0
```

### High Response Time Alert

Triggered when:

```text
ml_response_time > 1
```

---

## Technologies Used

| Category             | Technology          |
| -------------------- | ------------------- |
| Programming Language | Python              |
| Data Processing      | Pandas, NumPy       |
| Machine Learning     | Scikit-Learn        |
| Experiment Tracking  | MLflow              |
| Model Registry       | DagsHub             |
| Version Control      | GitHub              |
| CI/CD                | GitHub Actions      |
| Containerization     | Docker              |
| Monitoring           | Prometheus          |
| Visualization        | Grafana             |
| Logging              | Prometheus Exporter |

---

## Project Workflow

```text
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Experiment Tracking (MLflow)
   │
   ▼
Model Training & Evaluation
   │
   ▼
Model Registry (DagsHub)
   │
   ▼
Docker Deployment
   │
   ▼
MLflow Model Serving
   │
   ▼
Prometheus Monitoring
   │
   ▼
Grafana Dashboard
   │
   ▼
Alerting System
```

---

## Repository Structure

```text
Customer-Personality-MLOps-Monitoring-System
│
├── Eksperimen_ML
├── Model_Development
├── Workflow_CI
├── Monitoring_dan_Logging
└── README.md
```

---

## Project Achievements

### Experiment Tracking

✔ MLflow Experiment Tracking

### Machine Learning Model Development

✔ Model Training and Evaluation

### Model Registry

✔ DagsHub Integration

### CI/CD Workflow

✔ GitHub Actions Automation

### Deployment

✔ Docker Containerization
✔ MLflow Model Serving

### Monitoring and Logging

✔ Prometheus Monitoring
✔ Grafana Dashboard
✔ Alerting Configuration

---

## Learning Outcomes

Through this project, the following competencies were implemented:

* Machine Learning Lifecycle Management
* Data Preprocessing
* Experiment Tracking
* Model Development
* Model Deployment
* Docker Containerization
* CI/CD Workflow Automation
* Monitoring and Logging
* Metrics Collection
* Dashboard Development
* Alert Configuration
* End-to-End MLOps Implementation

---

## Author

**Shava Selvia Ramadhani Subekti**

Undergraduate Student in Informatics Engineering
State Polytechnic of Jember

### Areas of Interest

* Machine Learning
* Data Science
* Machine Learning Operations (MLOps)
* Artificial Intelligence
* Software Engineering
* UI/UX Design

### GitHub

@shavel28

---

## Academic Information

This repository was developed as part of the implementation of Machine Learning Operations (MLOps) concepts, covering experiment tracking, model development, deployment, workflow automation, monitoring, logging, and alerting using industry-standard tools and practices.

---

## License

This project is intended for educational, research, and portfolio purposes.

🌟 If you find this project useful, feel free to give it a star and explore the repository. Feedback, suggestions, and collaboration opportunities are always welcome.
