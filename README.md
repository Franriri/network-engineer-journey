# Network Engineer Journey

My hands-on study notes and labs on the way from Service Desk Specialist to Network and Cloud Engineer.
Everything here is practiced with **free tools** (AWS free tier, Cisco Packet Tracer, open-source software).

## Roadmap

| # | Module | Tools | Status |
|---|--------|-------|--------|
| 1 | Terminal and access tools | PowerShell, OpenSSH, AWS EC2 | Done |
| 2 | Simulators and emulators (labbing) | AWS VPC, Cisco Packet Tracer | Done |
| 3 | Traffic analysis and diagnostics | Wireshark, tcpdump, nmap | Next |
| 4 | Network automation and IaC | Python (Netmiko), Ansible, Terraform, AWS CLI | Planned |
| 5 | Monitoring and management | CloudWatch, Zabbix or Grafana, SNMP | Planned |
| 6 | Documentation and utilities | draw.io, Markdown, Git/GitHub, VS Code | Planned |

## Notes

- [Module 1: Terminal and access tools](docs/module-01-terminal-and-access.md)
- [Module 2, Part 1: Build a network in AWS](docs/module-02-part1-aws-vpc-lab.md)
- [Module 2, Part 2: Cisco Packet Tracer lab](docs/module-02-part2-packet-tracer-lab.md)
- [Command cheat sheet](docs/cheatsheet.md)
- [Cost-safety checklist](docs/cost-safety-checklist.md)
- [Learning log](journal/learning-log.md)

## Labs

- `labs/packet-tracer/` router and switch configurations (fictional company "Fran Corp")
- `labs/aws/` VPC lab checklist

## Security rules for this repository

- Never commit `.pem` or `.ppk` keys, passwords, or access keys (the `.gitignore` helps, but always double-check).
- Do not publish AWS account IDs, public IP addresses, or screenshots that show them.
- Lab passwords in this repo are fake placeholders.
