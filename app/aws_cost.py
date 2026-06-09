import boto3
from datetime import date

client = boto3.client("ce")


def get_cost_data():
    try:

        today = date.today()

        response = client.get_cost_and_usage(
            TimePeriod={
                "Start": today.replace(day=1).strftime("%Y-%m-%d"),
                "End": today.strftime("%Y-%m-%d")
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"]
        )

        amount = float(
            response["ResultsByTime"][0]["Total"]
            ["UnblendedCost"]["Amount"]
        )

        return {
            "status": "success",
            "total_cost": round(amount, 4),
            "data": response
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }