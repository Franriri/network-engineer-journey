# Module 2, Part 2: Cisco Packet Tracer Lab

**Analogy:** the switch is the hallway of the Finance floor. The router is the front door and post office of the building.

## Topology

```
FIN-PC01 (192.168.1.10) --Fa0/1--+
                                 |-- HQ-FIN-SW01 (192.168.1.2) --Gi0/1--Gi0/0/0-- HQ-RTR01 (192.168.1.1)
FIN-PC02 (192.168.1.11) --Fa0/2--+
```

Network: 192.168.1.0/24. Default gateway: 192.168.1.1. Naming pattern: location - role - number, with hyphens.

Configurations: see [`labs/packet-tracer`](../labs/packet-tracer/).

## Results

| Test | Result |
|---|---|
| PC to PC ping | 4 of 4, TTL=128 |
| PC to router ping | 4 of 4, TTL=255 |
| PC to switch ping | 3 of 4, first timed out (ARP) |
| `show ip route` | C 192.168.1.0/24, L 192.168.1.1/32 |
| `show mac address-table` | Entries are learned from traffic and expire |

## Key ideas

- A **switch** connects devices inside one LAN using MAC addresses. A **router** connects different networks using IP addresses.
- The first ping can time out because of **ARP** (finding the MAC address for an IP address).
- The three-way handshake belongs to TCP. Ping uses ICMP and has no handshake.
- TTL hints: 128 = Windows-type, 255 = Cisco, 64 = Linux.

## Packet Tracer vs AWS

| Packet Tracer | AWS |
|---|---|
| Router interface 192.168.1.1 (default gateway) | Route table 0.0.0.0/0 to the Internet Gateway, and the VPC router |
| Switch connecting PCs | Subnet connecting servers |
| Connected route (C) | The `local` route |
| Access rules | Security groups |
