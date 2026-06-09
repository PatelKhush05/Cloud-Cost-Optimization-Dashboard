from app.health_score import get_health_score
from app.budget import get_budget_status
from app.recommendations import get_recommendations
from app.cost_analysis import get_service_costs

def get_dashboard_data():
    return {
        "health_score": get_health_score(),
        "budget_status": get_budget_status(),
        "recommendations": get_recommendations(),
        "service_costs": get_service_costs()
    }