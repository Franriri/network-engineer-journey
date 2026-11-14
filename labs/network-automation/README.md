# Network configuration templates (Python and Jinja2)

One template (`router.j2`) plus a list of sites (in `generate_configs.py`) produces one router configuration per site.
Think of a form letter: write the letter once, keep a list of names, and print one letter per name.

## Run in AWS CloudShell

```
pip3 install --user jinja2     # only if jinja2 is missing
python3 generate_configs.py
cat br1-rtr01.txt
```

## Test in Cisco Packet Tracer

1. Add a router, a switch and a PC. Router Gi0/0/0 to switch Gi0/1, PC to switch Fa0/1.
2. Paste the generated `br1-rtr01.txt` into the router CLI (in small blocks).
3. PC: 192.168.2.10/24, gateway 192.168.2.1. Then `ping 192.168.2.1`.

Result: `show ip interface brief` showed Gi0/0/0 = 192.168.2.1 up/up, and the ping got 4 of 4 replies.

## Why data and template are separate

- Add a site by changing only the data. The template stays the same.
- Change the standard once in the template, and every site follows.
- Later the data can come from a spreadsheet or an inventory file.
