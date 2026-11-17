"""Netmiko demo: run read-only commands on a Linux EC2 server over SSH.
Written with AI assistance (Claude); run and tested by Fran.
The IP address and key path are typed in when the script runs, so no secrets are stored here.
"""
from netmiko import ConnectHandler
from datetime import datetime

host = input("Server public IP: ").strip()
key_file = input("Path to key file: ").strip().strip('"')

device = {
    "device_type": "linux",   # use "cisco_ios" for a Cisco router
    "host": host,
    "username": "ec2-user",
    "use_keys": True,
    "key_file": key_file,
}

commands = [
    "hostname",
    "uname -r",
    "ip -brief addr",
    "cat /proc/sys/net/ipv4/ip_default_ttl",
    "df -h /",
]

print("Connecting to", host, "...")
report = []
with ConnectHandler(**device) as conn:
    for cmd in commands:
        output = conn.send_command(cmd)
        block = "$ " + cmd + "\n" + output + "\n"
        print(block)
        report.append(block)

with open("report.txt", "w") as f:
    f.write("Report created " + datetime.now().isoformat(timespec="seconds") + "\n\n")
    f.write("\n".join(report))
print("Saved report.txt")
