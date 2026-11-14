"""Generate router configs from one Jinja2 template. Writes text files only.
Written with AI assistance (Claude); run and tested by Fran in AWS CloudShell and Cisco Packet Tracer.
"""
from jinja2 import Environment, FileSystemLoader

sites = [
    {"hostname": "HQ-RTR01", "interface": "GigabitEthernet0/0/0",
     "description": "LINK-TO-HQ-FIN-SW01", "ip": "192.168.1.1", "mask": "255.255.255.0"},
    {"hostname": "BR1-RTR01", "interface": "GigabitEthernet0/0/0",
     "description": "LINK-TO-BR1-SW01", "ip": "192.168.2.1", "mask": "255.255.255.0"},
    {"hostname": "BR2-RTR01", "interface": "GigabitEthernet0/0/0",
     "description": "LINK-TO-BR2-SW01", "ip": "192.168.3.1", "mask": "255.255.255.0"},
]

env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router.j2")

for site in sites:
    config = template.render(**site)
    filename = site["hostname"].lower() + ".txt"
    with open(filename, "w") as f:
        f.write(config + "\n")
    print("Created", filename)
