# Network Engineer Journey

My hands-on study notes and labs on the way from Service Desk Specialist to Network and Cloud Engineer.
Everything here is practiced with **free tools** (AWS free tier, Cisco Packet Tracer, open-source software).
Some scripts were written with AI assistance (Claude). I run, test and explain them myself, and each file says so.

## Roadmap

| # | Module | Tools | Status |
|---|--------|-------|--------|
| 1 | Terminal and access tools | PowerShell, OpenSSH, AWS EC2 | Done |
| 2 | Simulators and emulators (labbing) | AWS VPC, Cisco Packet Tracer | Done |
| 3 | Traffic analysis and diagnostics | Wireshark, tracert, AWS EC2 | Done |
| 4 | Network automation and IaC | AWS CLI, Python, Terraform, Jinja2 | In progress (Lab 5 next) |
| 5 | Monitoring and management | CloudWatch, Zabbix or Grafana, SNMP | Planned |
| 6 | Documentation and utilities | draw.io, Markdown, Git/GitHub, VS Code | Planned |

## Notes

- [Module 1: Terminal and access tools](docs/module-01-terminal-and-access.md)
- [Module 2, Part 1: Build a network in AWS](docs/module-02-part1-aws-vpc-lab.md)
- [Module 2, Part 2: Cisco Packet Tracer lab](docs/module-02-part2-packet-tracer-lab.md)
- [Module 3: Traffic analysis with Wireshark](docs/module-03-wireshark-labs.md)
- [Module 4: Network automation and IaC](docs/module-04-network-automation-iac.md)
- [Command cheat sheet](docs/cheatsheet.md)
- [Cost-safety checklist](docs/cost-safety-checklist.md)
- [Learning log](journal/learning-log.md)

## Code and labs

- `scripts/` read-only AWS cost-safety checker (Python, boto3)
- `labs/packet-tracer/` router and switch configurations (fictional company "Fran Corp")
- `labs/aws/` VPC lab checklist
- `labs/terraform/` VPC built from code
- `labs/network-automation/` configuration templates (Python and Jinja2)

## Security rules for this repository

- Never commit `.pem` or `.ppk` keys, passwords, or access keys.
- Never commit packet captures (`.pcap`, `.pcapng`) or Terraform state (`.tfstate`, `.terraform`).
- Do not publish AWS account IDs, public IP addresses, or screenshots that show them.
- Lab passwords in this repo are fake placeholders.
