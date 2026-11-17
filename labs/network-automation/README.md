# Network automation with Python

## Part 1: configuration templates (Python and Jinja2)

One template (`router.j2`) plus a list of sites (in `generate_configs.py`) produces one router configuration per site.
Think of a form letter: write the letter once, keep a list of names, and print one letter per name.

Run in AWS CloudShell:

```
pip3 install --user jinja2     # only if jinja2 is missing
python3 generate_configs.py
cat br1-rtr01.txt
```

Test in Cisco Packet Tracer: paste `br1-rtr01.txt` into a new router, set a PC to 192.168.2.10/24 with gateway 192.168.2.1, then ping 192.168.2.1.
Result: `show ip interface brief` showed Gi0/0/0 = 192.168.2.1 up/up, and the ping got 4 of 4 replies.

Why data and template are separate: add a site by changing only the data, change the standard once in the template, and later feed the data from a spreadsheet or inventory.

## Part 2: Netmiko (SSH to a Linux server)

`netmiko_check.py` connects to a Linux EC2 server over SSH, runs five read-only commands and saves `report.txt`.
For a Cisco router, change `device_type` to `cisco_ios`.

Run on Windows (Python 3.13 was used, because the newest Python was not yet supported by all dependencies):

```
python -m pip install netmiko
py -V:3.13 netmiko_check.py
```

The script asks for the server's public IP and the key path, so no secrets are stored in the file.
Never upload `report.txt` or any `.pem` key.
