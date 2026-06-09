from app.cost_analysis import get_service_costs


def get_health_score():

    data = get_service_costs()

    if data["status"] != "success":
        return data

    services = data["services"]

    if not services:
        return {
            "status": "success",
            "health_score": None,
            "rating": "No cost data available"
        }

    score = 100

    if services.get("Amazon EC2", 0) > 10:
        score -= 10

    if services.get("Amazon S3", 0) > 2:
        score -= 5

    if services.get("Amazon RDS", 0) > 5:
        score -= 10

    if services.get("AWS Lambda", 0) > 1:
        score -= 5

    if score >= 85:
        rating = "Excellent"
    elif score >= 70:
        rating = "Good"
    elif score >= 50:
        rating = "Average"
    else:
        rating = "Needs Optimization"

    return {
        "status": "success",
        "health_score": score,
        "rating": rating
    }