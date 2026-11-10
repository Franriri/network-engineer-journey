# Cost-safety checklist

1. Create a budget alert before launching resources.
2. Choose only instance types marked **Free tier eligible**, and start small.
3. Open SSH only to **My IP**.
4. Terminate EC2 instances when the lab ends and confirm the state is **Terminated**.
5. Check for leftover Elastic IPs and NAT Gateways.
6. Never share .pem files, account IDs, or screenshots showing them.

Free to keep: VPC, subnets, route tables, Internet Gateway, security groups.
Can cost money: running EC2 instances, public IPv4 addresses in use, Elastic IPs, NAT Gateways.
