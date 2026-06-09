from app.cost_analysis import get_service_costs


def get_recommendations():

    data = get_service_costs()

    if data["status"] != "success":
        return data

    services = data["services"]

    recommendations = []

    if services.get("Amazon EC2", 0) > 10:
        recommendations.append(
            "Review EC2 instance sizing to reduce costs."
        )

    if services.get("Amazon S3", 0) > 2:
        recommendations.append(
            "Enable S3 lifecycle policies."
        )

    if services.get("Amazon RDS", 0) > 5:
        recommendations.append(
            "Review unused RDS instances."
        )

    if services.get("AWS Lambda", 0) > 1:
        recommendations.append(
            "Monitor Lambda execution costs."
        )

    return {
    "status": "success",
    "recommendations": recommendations,
    "count": len(recommendations)
}