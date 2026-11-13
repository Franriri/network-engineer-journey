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
