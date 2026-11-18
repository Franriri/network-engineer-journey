# Command cheat sheet

## Linux (EC2)
| Command | Meaning |
|---|---|
| `whoami` | Current user |
| `pwd` | Current folder |
| `ip addr` | Interfaces and IP addresses |
| `ping -c 4 <ip>` | Send 4 pings |
| `traceroute <ip>` | Path to destination (UDP by default) |
| `sudo traceroute -I <ip>` | Traceroute using ICMP |
| `df -h` | Disk space |
| `cat /proc/sys/net/ipv4/ip_default_ttl` | Default TTL of this server |
| `curl localhost` | Test the local web server |

## Windows PowerShell
| Command | Meaning |
|---|---|
| `cd "path with spaces"` | Change folder (use quotes) |
| `ssh -i key.pem ec2-user@<server-public-ip>` | Connect to EC2 (use the server's IP, not your own) |
| `ipconfig` | Show IP settings |
| `tracert <ip>` | Path to a destination |
| `nslookup <name>` | DNS lookup |
| `Test-Path $key` | Check that a path exists |

## Cisco IOS
| Command | Meaning |
|---|---|
| `enable` | Privileged mode |
| `configure terminal` | Configuration mode |
| `hostname <name>` | Set device name |
| `interface <port>` | Select a port |
| `ip address <ip> <mask>` | Set an address |
| `no shutdown` | Turn a port on |
| `show ip interface brief` | Port and IP summary |
| `show ip route` | Routing table |
| `show mac address-table` | Switch MAC table |
| `snmp-server community <string> RO` | SNMP v2c read-only community |
| `copy running-config startup-config` | Save the configuration |
| `?` and Tab | Help and autocomplete |

## TTL hints
| Start value | Usually means |
|---|---|
| 128 | Windows |
| 255 | Cisco devices |
| 127 | Amazon Linux 2023 |
| 64 | Many other Linux systems |

## Wireshark display filters
| Filter | Use |
|---|---|
| `icmp`, `dns`, `arp` | One protocol |
| `http.request` | HTTP requests |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | New TCP connections |
| `ip.addr == <ip>` | Traffic to or from one IP |
| `tcp.port == 22` | SSH traffic |

## AWS CloudShell
| Command | Meaning |
|---|---|
| `export AWS_PAGER=""` | Stop the (END) pager (or press `q`) |
| `aws ec2 describe-vpcs --output table` | Read VPCs (describe commands only read) |
| `aws cloudwatch list-metrics --namespace AWS/EC2` | List EC2 metrics |
| `aws cloudwatch get-metric-statistics ...` | Read metric data points |
| `aws cloudwatch describe-alarms` | List alarms |
| `aws sns list-topics` | List SNS topics |
| `python3 ~/cost_check.py` | Cost-safety report after every lab |
| `df -h ~` | CloudShell home space (limit 1 GB) |
| `du -sh ~/* ~/.[!.]* \| sort -h \| tail` | What uses the space |

## Looking at files and scripts (CloudShell)
| Command | Meaning |
|---|---|
| `ls -lha` | List files with details, including hidden ones |
| `find ~ -maxdepth 2 -name "*.py"` | Find Python scripts |
| `cat -n file` | Show a file with line numbers |
| `less file` | Read a long file page by page (`q` to quit) |
| `grep -n "word" file` | Search inside a file |
| `python3 -m py_compile file.py` | Check for typing errors without running |
| `python3 file.py` | Run a script |
| `history \| tail -30` | Last 30 commands |
