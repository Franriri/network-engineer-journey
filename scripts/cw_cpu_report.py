"""Print CPU utilization of an EC2 instance from CloudWatch (READ-ONLY).
Written with AI assistance (Claude); run and verified by Fran in AWS CloudShell.
"""
import os
from datetime import datetime, timedelta, timezone
import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-2")
cw = boto3.client("cloudwatch", region_name=REGION)

instance_id = input("Instance ID (for example i-0123456789abcdef0): ").strip()
hours = int(input("How many hours back? [24]: ").strip() or "24")

end = datetime.now(timezone.utc)
start = end - timedelta(hours=hours)

resp = cw.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
    StartTime=start,
    EndTime=end,
    Period=300,
    Statistics=["Average", "Maximum"],
)

points = sorted(resp["Datapoints"], key=lambda p: p["Timestamp"])
print("\nCPU report for", instance_id, "in", REGION)
if not points:
    print("No data points found. Check the instance ID and the time range.")
else:
    print("Time (UTC)           Avg %   Max %  Graph")
    for p in points:
        t = p["Timestamp"].strftime("%Y-%m-%d %H:%M")
        bar = "#" * int(p["Average"] / 2)
        print(f"{t}  {p['Average']:6.1f}  {p['Maximum']:6.1f}  {bar}")
    avg_all = sum(p["Average"] for p in points) / len(points)
    peak = max(p["Maximum"] for p in points)
    print("\nData points:", len(points), "| Overall average:", round(avg_all, 1), "% | Peak:", round(peak, 1), "%")
    if peak > 70:
        print("NOTE: the peak went above 70%, which would have triggered our alarm.")
    else:
        print("The CPU stayed below 70%, so our alarm would not have fired.")
