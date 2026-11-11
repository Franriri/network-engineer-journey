# Module 3, Part 1: Traffic Analysis with Wireshark (Lab 1)

**Analogy:** Wireshark is a security camera for the network cable. It records packets and shows them in readable form.

## Key terms

| Term | Meaning |
|---|---|
| Capture filter | Decides what to record (before capturing) |
| Display filter | Decides what to show from the recording |
| DNS A / AAAA | IPv4 address / IPv6 address |
| TTL | Counter that drops by 1 at each router |

## Lab 1 (free, on my PC)

1. Install Wireshark from wireshark.org. Skip USBPcap. Keep Npcap.
2. Capture on the Wi-Fi interface (the one with the moving graph line).
3. Generate traffic: `ping 8.8.8.8` and `nslookup google.com`. Stop the capture.
4. Use display filters.

| Filter | Result (of 2125 packets) |
|---|---|
| `dns` | 46 |
| `arp` | 14 |
| `icmp` | 8 (4 requests + 4 replies) |
| `tcp.flags.syn == 1` | 29 (SYN and SYN-ACK) |

## Findings

- Ping request: private PC address to 8.8.8.8, TTL 128 (Windows-type). Reply TTL 115.
- Status bar: Packets = captured, Displayed = matches the filter, Dropped = missed.
- DNS answer for google.com (A record): an IPv4 address. The AAAA query returned an IPv6 address.
- The destination MAC of the ping was my home router. The MAC changes at each hop, the IP stays the same.
- `tracert 8.8.8.8` took 11 hops: home router, ISP routers, Google network, destination.

## Lessons

- "Request In" is the packet number of the question, not the answer. The IP is under Answers (addr).
- A TTL estimate is only a clue. The return path can differ. Tracert shows the real path.
- `tcp.flags.syn == 1` also counts SYN-ACK. Use `&& tcp.flags.ack == 0` for new connections only.
- A Wi-Fi capture includes background apps.

## Useful filters

```
icmp
dns
arp
tcp.flags.syn == 1 && tcp.flags.ack == 0
dns.qry.name == "google.com"
ip.addr == <server-ip>
tcp.port == 22
```

## Safety

Capture only my own network. Never upload `.pcap` files or screenshots with personal data to GitHub.

## Next

Lab 2: web server on an EC2 instance, capture the TCP three-way handshake, and compare plain text with encrypted SSH.
