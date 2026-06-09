from fastapi import FastAPI

from app.aws_cost import get_cost_data
from app.recommendations import get_recommendations
from app.health_score import get_health_score
from app.budget import get_budget_status
from app.cost_analysis import get_service_costs
from app.dashboard import get_dashboard_data

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Cloud Cost Optimization Dashboard",
        "status": "Running"
    }


@app.get("/cost")
def cost():
    return get_cost_data()


@app.get("/service-costs")
def service_costs():
    return get_service_costs()


@app.get("/recommendations")
def recommendations():
    return get_recommendations()


@app.get("/health-score")
def health_score():
    return get_health_score()


@app.get("/budget-status")
def budget_status():
    return get_budget_status()

@app.get("/dashboard")
def dashboard():
    return get_dashboard_data()