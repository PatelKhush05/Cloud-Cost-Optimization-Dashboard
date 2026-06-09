# 🚀 Cloud Cost Optimization Dashboard

## Overview

Cloud Cost Optimization Dashboard is a cloud monitoring and cost analysis platform built using FastAPI, AWS Cost Explorer, Grafana, and Docker.

The application collects AWS billing and usage data, analyzes cloud spending patterns, evaluates budget utilization, generates optimization recommendations, and visualizes key metrics through an interactive Grafana dashboard.

This project demonstrates practical cloud engineering, API development, monitoring, and cost optimization concepts commonly used in modern DevOps and FinOps environments.

---

## ✨ Key Features

### AWS Cost Monitoring

* Integrates with AWS Cost Explorer using Boto3
* Retrieves cloud spending data
* Tracks AWS usage costs

### Cost Analysis

* Service-wise cost breakdown
* Cloud expenditure visibility
* Budget consumption analysis

### Budget Management

* Budget utilization tracking
* Remaining budget calculation
* Cost threshold monitoring

### Optimization Recommendations

* Generates cloud cost optimization insights
* Identifies potential cost-saving opportunities
* Encourages efficient resource utilization

### Cloud Health Score

* Calculates infrastructure cost efficiency
* Provides overall cloud cost health assessment
* Highlights optimization requirements

### Dashboard Visualization

* Interactive Grafana dashboards
* Real-time metric visualization
* Cloud cost monitoring interface

### Containerization

* Dockerized deployment
* Portable and scalable architecture

---

## 🛠️ Technology Stack

| Category          | Technologies      |
| ----------------- | ----------------- |
| Backend           | Python, FastAPI   |
| Cloud             | AWS Cost Explorer |
| AWS SDK           | Boto3             |
| Monitoring        | Grafana           |
| Containerization  | Docker            |
| API Documentation | Swagger UI        |

---

## 🏗️ System Architecture

```text
AWS Cost Explorer
        │
        ▼
FastAPI Backend
        │
        ▼
Cost Analysis Engine
        │
        ▼
REST APIs
        │
        ▼
Grafana Dashboard
```

---

## 🔗 API Endpoints

| Endpoint           | Description                       |
| ------------------ | --------------------------------- |
| `/`                | Application Status                |
| `/cost`            | Retrieve AWS Cost Data            |
| `/service-costs`   | Service-Level Cost Analysis       |
| `/budget-status`   | Budget Monitoring                 |
| `/health-score`    | Cost Health Score                 |
| `/recommendations` | Cost Optimization Recommendations |
| `/dashboard`       | Consolidated Dashboard Data       |

---

## 📊 Dashboard Metrics

The Grafana dashboard provides visibility into:

* Current Cloud Spend
* Remaining Budget
* Budget Limit
* Health Score
* Cost Optimization Recommendations
* Service-Level Cost Distribution

---

## 📸 Screenshots

### Grafana Dashboard

<img src="screenshots/grafana-dashboard.png" width="900">

### FastAPI Swagger Documentation

<img src="screenshots/fastapi-swagger.png" width="900">

---

## 🎯 Learning Outcomes

This project helped develop practical experience in:

* Cloud Cost Management
* AWS Cost Explorer Integration
* REST API Development
* FastAPI Framework
* Infrastructure Monitoring
* Grafana Dashboards
* Docker Containerization
* Cloud Financial Operations (FinOps)

---

## 🚀 Future Enhancements

* AWS Budgets Integration
* Email Alerting System
* CloudWatch Integration
* Multi-Account AWS Monitoring
* Cost Forecasting
* Automated Cost Optimization Reports
* Role-Based Access Control (RBAC)

---

## 👨‍💻 Author

**Khush Patel**

Cloud & DevOps Engineering (Aspiring)

Focused on Cloud Computing, DevOps, Automation, Infrastructure Monitoring, and Cost Optimization Solutions.
