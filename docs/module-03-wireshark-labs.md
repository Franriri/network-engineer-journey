# Module 3: Traffic Analysis with Wireshark

**Analogy:** Wireshark is a security camera for the network cable. It records packets and shows them in readable form.

## Key terms

| Term | Meaning |
|---|---|
| Capture filter | Decides what to record (before capturing) |
| Display filter | Decides what to show from the recording |
| DNS A / AAAA | IPv4 address / IPv6 address |
| TTL | Counter that drops by 1 at each router |
| TCP three-way handshake | SYN (client), SYN-ACK (server), ACK (client) |

## Lab 1: capture on my PC (free)

1. Install Wireshark from wireshark.org. Skip USBPcap. Keep Npcap.
2. Capture on the Wi-Fi interface. Run `ping 8.8.8.8` and `nslookup google.com`. Stop the capture.

| Filter | Result (of 2125 packets) |
|---|---|
| `dns` | 46 |
| `arp` | 14 |
| `icmp` | 8 (4 requests + 4 replies) |
| `tcp.flags.syn == 1` | 29 (SYN and SYN-ACK) |

Findings:
- Ping request TTL 128 (Windows PC), reply TTL 115.
- Status bar: Packets = captured, Displayed = matches the filter, Dropped = missed.
- DNS answer is under Answers (`addr`), not in "Request In".
- The destination MAC of the ping was my home router.
- `tracert 8.8.8.8` took 11 hops.

## Lab 2: web server on AWS EC2 (terminated afterwards)

1. Launch a `t3.micro` in `lab-vpc`, `public-subnet`, `public-sg`. Add an HTTP rule with source **My IP**.
2. SSH in with the **server's** public IP and run, one by one:

```
sudo dnf install -y httpd
echo "Hello from Fran's lab" | sudo tee /var/www/html/index.html
sudo systemctl enable --now httpd
curl localhost
```

3. Start the Wireshark capture **before** opening `http://<server-ip>`. Filter: `ip.addr == <server-ip> && tcp.port == 80`.

Results:

| What I captured | Meaning |
|---|---|
| `[SYN]`, `[SYN, ACK]`, `[ACK]` (Len=0) | The handshake opens the connection and carries no data |
| `GET / HTTP/1.1` then `HTTP/1.1 200 OK` | The page was delivered. `favicon.ico` returned 404 (normal) |
| Follow TCP Stream (HTTP) | Page text and server software are readable (plain text) |
| Follow TCP Stream (SSH) | Readable greeting, then encrypted data |
| SYN to SYN-ACK about 216 ms | Round-trip time to the server in Sydney |
| Server TTL 119 | Amazon Linux 2023 starts at 127, so about 8 hops |

## TTL hints (corrected)

| Start value | Usually means |
|---|---|
| 128 | Windows |
| 255 | Cisco devices |
| 127 | Amazon Linux 2023 |
| 64 | Many other Linux systems |

These are clues, not proof. I first assumed Linux would start at 64. Amazon Linux 2023 starts at 127 (confirmed with `cat /proc/sys/net/ipv4/ip_default_ttl`).

## Quick check (polished)

- Handshake: the client sends SYN, the server replies with SYN-ACK, the client confirms with ACK.
- HTTP sends data in plain text. SSH encrypts it. HTTPS also encrypts, but it is a different protocol (TLS).
- Port 80 was opened to My IP only, so only my PC can reach the test server (least privilege).

## Useful filters

```
icmp
dns
http.request
tcp.flags.syn == 1 && tcp.flags.ack == 0
dns.qry.name == "google.com"
ip.addr == <server-ip> && tcp.port == 80
tcp.port == 22
```

## Safety and cost

Capture only my own network. Never upload `.pcap` or `.pcapng` files. Terminate the EC2 server, delete temporary security group rules, and check Elastic IPs, NAT Gateways and Volumes.
