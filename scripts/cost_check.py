"""Cost-safety checker: READ-ONLY. It only uses describe calls."""
import os
import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-2")
ec2 = boto3.client("ec2", region_name=REGION)
problems = 0

print("Cost-safety report for region:", REGION)

# 1. EC2 instances that are not terminated
print("\n=== 1. EC2 instances ===")
found = False
for page in ec2.get_paginator("describe_instances").paginate():
    for reservation in page["Reservations"]:
        for inst in reservation["Instances"]:
            state = inst["State"]["Name"]
            if state != "terminated":
                found = True
                problems += 1
                name = next((t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"), "(no name)")
                print("  WARNING:", inst["InstanceId"], name, inst["InstanceType"], state)
if not found:
    print("  OK: no running, stopped or pending instances")

# 2. Elastic IP addresses
print("\n=== 2. Elastic IPs ===")
addresses = ec2.describe_addresses()["Addresses"]
for a in addresses:
    problems += 1
    print("  WARNING:", a.get("PublicIp"), "is allocated")
if not addresses:
    print("  OK: no Elastic IPs")

# 3. NAT gateways that are active
print("\n=== 3. NAT gateways ===")
nats = ec2.describe_nat_gateways(
    Filter=[{"Name": "state", "Values": ["pending", "available"]}]
)["NatGateways"]
for n in nats:
    problems += 1
    print("  WARNING:", n["NatGatewayId"], n["State"])
if not nats:
    print("  OK: no active NAT gateways")

# 4. EBS volumes
print("\n=== 4. Volumes ===")
volumes = ec2.describe_volumes()["Volumes"]
for v in volumes:
    problems += 1
    print("  WARNING:", v["VolumeId"], str(v["Size"]) + " GB", v["State"])
if not volumes:
    print("  OK: no volumes")

# Summary
print("\n=== Summary ===")
if problems == 0:
    print("ALL CLEAR: nothing is left that could cost money.")
else:
    print(problems, "item(s) need a look. Check them in the console.")
