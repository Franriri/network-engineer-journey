# Module 2, Part 1: Build a Network in AWS

**Analogy:** a VPC is a gated village. Subnets are neighborhoods. The Internet Gateway is the main gate. Route tables are road signs. Security groups are guards with a guest list.

## Design

| Resource | Value |
|---|---|
| VPC | `lab-vpc`, 10.0.0.0/16 |
| Public subnet | `public-subnet`, 10.0.1.0/24, auto-assign public IPv4 on |
| Private subnet | `private-subnet`, 10.0.2.0/24 |
| Internet Gateway | `lab-igw`, attached to `lab-vpc` |
| Route table | `public-rt`: 0.0.0.0/0 to `lab-igw`, linked to the public subnet |
| Security groups | `public-sg`: SSH from My IP. `private-sg`: All ICMP IPv4 from `public-sg` |
| Servers | `public-server` (public subnet, public IP), `private-server` (private subnet, no public IP) |

A subnet is **public** when its route table sends 0.0.0.0/0 to an Internet Gateway.

## Tests and results

| Test | Result |
|---|---|
| `ping -c 4 <private-ip>` from public-server | 4 of 4 replies |
| `ping -c 4 8.8.8.8` from public-server | 4 of 4 replies |
| `ping <private-ip>` from my own PC | Timed out (correct, address is private) |
| `traceroute <private-ip>` | Only stars (UDP blocked by private-sg) |
| `sudo traceroute -I <private-ip>` | ICMP mode passes the security group |

## Lessons

- A security group can make a healthy network look broken. Ask which guard blocks this kind of traffic.
- SSH timeouts are often caused by a changed IP address in the My IP rule.
- Avoid the "VPC and more" wizard. It can create a NAT Gateway, which costs money per hour.
- Free to keep: VPC, subnets, route tables, IGW, security groups. Terminate EC2 instances after each lab.
