# Learning log

## 2026-11-06 | Module 1
Launched an EC2 server and connected with SSH. Set a budget alert. Learned the loopback and broadcast addresses.

## 2026-11-08 | Module 2, Part 1
Built a VPC with public and private subnets, an Internet Gateway, a route table and security groups. Fixed an SSH timeout (My IP changed). Learned why traceroute showed only stars.

## 2026-11-09 | Module 2, Part 2
Built an HQ Finance LAN in Cisco Packet Tracer with CLI configuration. Learned ARP, MAC tables and TTL values.

## 2026-11-10 | GitHub
Created this repository and uploaded the Module 1 and 2 notes and labs.

## 2026-11-11 | Module 3, Lab 1
Captured traffic with Wireshark and used display filters (icmp, dns, arp, tcp.flags.syn). Read TTL and DNS answers. Traced the path to 8.8.8.8 (11 hops).

## 2026-11-12 | Module 3, Lab 2
Built a web server on EC2 and captured the TCP three-way handshake. Compared plain-text HTTP with encrypted SSH. Learned that Amazon Linux 2023 starts TTL at 127. Terminated all resources afterwards.

## 2026-11-13 | Module 4, Labs 1 to 3
Used the AWS CLI in CloudShell (read-only). Ran a Python cost-safety checker written with Claude. Built a VPC with Terraform, verified it and destroyed it. Fixed the CloudShell 1 GB storage limit by moving Terraform data to /tmp.

## 2026-11-14 | Module 4, Lab 4
Generated router configurations from one Jinja2 template and tested the BR1 config in Packet Tracer (interface up, ping 4 of 4).

## Next
Module 4, Lab 5: Netmiko and an Ansible introduction.
