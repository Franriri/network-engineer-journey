# Module 1: Terminal and Access Tools

**Goal:** connect securely to a cloud server with SSH and run basic network commands.

## Key concepts

| Term | Meaning |
|---|---|
| Terminal emulator | A text window for typing commands (PowerShell, Windows Terminal, PuTTY) |
| SSH | Encrypted remote login, TCP port 22 |
| Telnet | Old and unsafe, plain text, port 23 |
| Key pair | Public key on the server, private key (.pem) stays with me |
| EC2 | AWS virtual servers (instances) |
| AMI | The operating system template (Amazon Linux 2023) |
| Security group | A virtual firewall on the server |

## Lab summary

1. Create a monthly cost budget (Billing and Cost Management, Budgets).
2. Launch an EC2 `t3.micro` (free tier eligible), Amazon Linux 2023, new key pair, SSH allowed from **My IP** only.
3. Connect from PowerShell:

```powershell
cd "$HOME\Desktop\Networking AWS Journey\RSA"
ssh -i lab-key.pem ec2-user@<public-ip>
```

4. Practice commands: `whoami`, `pwd`, `ip addr`, `ping -c 4 8.8.8.8`, `traceroute 8.8.8.8`, `df -h`, `exit`.
5. Terminate the instance.

## What I learned

- `ping -c 4` stops after 4 packets on Linux. Without `-c`, Linux ping runs until Ctrl + C.
- `lo` is the loopback interface (127.0.0.1). `brd` is the broadcast address.
- A traceroute shows each router (hop) on the path.
- Allowing SSH only from My IP follows the principle of least privilege.

## Troubleshooting

| Problem | Fix |
|---|---|
| UNPROTECTED PRIVATE KEY FILE (Windows) | Fix permissions with `icacls.exe` on the key file |
| Connection timed out | My IP changed. Edit the SSH rule in the security group and choose My IP again |
| Permission denied (publickey) | Check the username (`ec2-user`) and the key file |
| `cd` fails with spaces | Put the path in quotes |
