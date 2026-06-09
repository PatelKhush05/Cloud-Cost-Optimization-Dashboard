import boto3
from datetime import date, timedelta

client = boto3.client("ce")


def get_service_costs():
    try:
        end_date = date.today()
        start_date = end_date - timedelta(days=30)

        response = client.get_cost_and_usage(
            TimePeriod={
                "Start": str(start_date),
                "End": str(end_date)
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE"
                }
            ]
        )

        service_costs = {}

        if response["ResultsByTime"]:
            for group in response["ResultsByTime"][0]["Groups"]:
                service_name = group["Keys"][0]
                cost = float(
                    group["Metrics"]["UnblendedCost"]["Amount"]
                )

                service_costs[service_name] = round(cost, 2)

        return {
            "status": "success",
            "services": service_costs
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }