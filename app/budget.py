from app.cost_analysis import get_service_costs
from app.aws_cost import get_cost_data


def get_budget_status():

    data = get_service_costs()

    if data["status"] != "success":
        return data

    services = data["services"]

    if services:
        current_spend = sum(services.values())
    else:
        cost_data = get_cost_data()

        if cost_data["status"] == "success":
            current_spend = cost_data["total_cost"]
        else:
            current_spend = 0

    budget_limit = 50

    if current_spend >= budget_limit:
        status = "Budget Exceeded"
    elif current_spend >= budget_limit * 0.8:
        status = "Budget Warning"
    else:
        status = "Within Budget"

    return {
        "status": status,
        "budget_limit": budget_limit,
        "current_spend": round(current_spend, 4),
        "remaining_budget": round(
            budget_limit - current_spend,
            4
        )
    }