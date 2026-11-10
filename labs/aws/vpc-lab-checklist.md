# AWS VPC lab checklist

- [ ] Budget alert created
- [ ] VPC `lab-vpc` 10.0.0.0/16 (no IPv6, default tenancy)
- [ ] Subnets 10.0.1.0/24 and 10.0.2.0/24 in the same Availability Zone
- [ ] Auto-assign public IPv4 on the public subnet only
- [ ] Internet Gateway created and attached
- [ ] Route table with 0.0.0.0/0 to the IGW, linked to the public subnet
- [ ] Security groups created (public-sg first)
- [ ] Two EC2 instances launched in the right subnets (check VPC and subnet before launching)
- [ ] Tests done (ping, ip addr, traceroute)
- [ ] **EC2 instances terminated**
- [ ] No Elastic IPs and no NAT Gateways
