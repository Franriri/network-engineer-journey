# Module 5: Monitoring and Management

**Analogy:** a car dashboard. You watch the speed, the temperature and the warning lights without opening the engine.

## Key terms

| Term | Meaning |
|---|---|
| Metric | A number measured over time (for example CPU %) |
| Alarm | A rule that notifies me when a threshold is met |
| Dashboard | One screen with my favorite graphs |
| SNS topic | A mailing list that CloudWatch uses to send the warning |
| SNMP | Simple Network Management Protocol: a monitoring tool reads status from network devices |
| Community string | The shared "password" of SNMP v1 and v2c, sent in plain text |
| OID / MIB | The address of one piece of information / the dictionary that explains OIDs |

## Labs

| Lab | What I did | Result |
|---|---|---|
| 1 | CloudWatch on an EC2 `t3.micro`: metrics, a Standard SNS topic with an email subscription, and a CPU alarm (above 70%, 5-minute period) | Alarm chain built, then everything cleaned up. The optional CPU load test was skipped because I was on a temporary device. |
| 2 | Read CloudWatch metrics with the AWS CLI and [`scripts/cw_cpu_report.py`](../scripts/cw_cpu_report.py) | Read the CPU data of a terminated server. Confirmed 0 alarms and 0 SNS topics afterwards. |
| 3 | SNMP v2c read-only on a router in Packet Tracer ([`labs/packet-tracer/snmp-router.txt`](../labs/packet-tracer/snmp-router.txt)), polled with the MIB Browser | sysName returned the router name |
| 4 | Zabbix and Grafana tour | Skipped for now, to study another time |

The Python script was written with AI assistance (Claude). I ran it and verified the results.

## Problems solved

| Problem | Cause | Fix |
|---|---|---|
| SNS dropdown had no Email option | I had created a FIFO topic (`.fifo`) | Create a Standard topic. The type cannot be changed later. |
| "All metrics" was missing | New CloudWatch menu | Metrics, then Classic metrics (or the Monitoring tab in EC2) |
| CloudShell home 98% full | An old Terraform project kept a 761 MB `.terraform` folder | Look with `du`, delete only the recreatable provider cache, keep the state file |
| `snmp-server location` gave "Invalid input" | Packet Tracer supports only part of the real commands | Skip it. The `community` line is what matters. |
| SSH path not found on a temporary device | The key folder was in a different location and the user name was different | Copy the exact path from File Explorer. Remove the key afterwards. |

## Quick check (polished)

- A metric is a number measured over time. An alarm is a rule that notifies the engineer when a threshold is met.
- The subscription must be confirmed to prove that the owner of the email address agrees to receive the messages (consent, not least privilege).
- Detailed monitoring (1-minute data) is charged, so I used basic monitoring (5-minute data, free).
- `--period 300` means 300 seconds, so each data point summarizes 5 minutes.
- CloudWatch stores metrics separately from the server, so the data stays after termination. As far as I know, 5-minute data points are kept for about 63 days.
- The lab was free and safe because the commands only read data and nothing was left running.
- SNMP lets a monitoring tool read status information (name, uptime, interface status, counters) from network devices.
- SNMP v1 and v2c send the community string in plain text. SNMP v3 adds authentication and encryption.
- `RO` means read-only, so the tool can view but not change settings (least privilege).

## Tools to study later

| Tool | Job |
|---|---|
| Zabbix | All-in-one monitoring server (polls devices with SNMP, uses agents, sends alerts) |
| Grafana | Draws dashboards from data sources such as CloudWatch, Prometheus and Zabbix |
| Prometheus | Collects and stores metrics |

## Safety

No access keys were created. Keys are removed from temporary devices. Alarms, SNS topics and servers were deleted after the labs, and `scripts/cost_check.py` confirmed ALL CLEAR.
