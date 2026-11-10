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

## Windows PowerShell
| Command | Meaning |
|---|---|
| `cd "path with spaces"` | Change folder (use quotes) |
| `ssh -i key.pem ec2-user@<ip>` | Connect to EC2 |
| `ipconfig` | Show IP settings |

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
| `copy running-config startup-config` | Save the configuration |
| `?` and Tab | Help and autocomplete |
