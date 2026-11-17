# Module 4: Network Automation and Infrastructure as Code

**Analogy:** clicking in the console is cooking from memory. Automation is a recipe that gives the same meal every time.

## Key terms

| Term | Meaning |
|---|---|
| CLI | Controlling AWS with typed commands |
| API / SDK (boto3) | The menu AWS offers to programs / the Python library that uses it |
| IaC | Infrastructure as Code: describe infrastructure in files |
| Terraform | Free IaC tool: write what you want, it builds it |
| Jinja2 template | A form letter with blanks that data fills in |
| Netmiko | Python library that runs commands on devices over SSH |
| Ansible | Describes the state you want in a playbook and makes the target match it |
| Idempotent | Running it again is safe. It only changes what is different |

## Labs

| Lab | Tool | What I did | Result |
|---|---|---|---|
| 1 | AWS CLI in CloudShell | Read-only `describe` commands, `--query`, `--output table` | VPCs, subnets and the four cost-safety checks |
| 2 | Python and boto3 | [`scripts/cost_check.py`](../scripts/cost_check.py) runs the four checks at once | ALL CLEAR |
| 3 | Terraform | [`labs/terraform`](../labs/terraform/): init, plan (7 to add), apply, verify, plan (No changes), destroy | VPC built from code and destroyed |
| 4 | Python and Jinja2 | [`labs/network-automation`](../labs/network-automation/): one template, three router configs | BR1 config tested in Packet Tracer, ping 4 of 4 |
| 5A | Netmiko | `netmiko_check.py` ran five commands on a Linux server over SSH | Default TTL 127, matching Module 3 |
| 5B | Ansible | [`labs/ansible`](../labs/ansible/): ping, playbook, `--check`, run twice | changed=2, then changed=0 |

The Python, Terraform, Jinja2, Netmiko and Ansible files were written with AI assistance (Claude). I ran, tested and explained them.

## Problems solved

| Problem | Cause | Fix |
|---|---|---|
| Output stuck at `(END)` | The CLI opened a pager | Press `q`, or `export AWS_PAGER=""` |
| `terraform init`: no space left on device | CloudShell home is 1 GB and the AWS provider is large | Keep Terraform data in /tmp with `TF_DATA_DIR` and `TF_PLUGIN_CACHE_DIR` |
| Netmiko install failed on Python 3.15 | Very new Python versions lag behind some libraries | Install Python 3.13 and run with `py -V:3.13` |
| SSH timeout | Used my own IP instead of the server's, or My IP changed | Use the server's public IP and refresh the security group rule |
| Home folder 98% full | Leftover Terraform files | Install Ansible in a /tmp virtual environment and delete caches |

## Quick check (polished)

- IaC lets you configure infrastructure with code instead of manual clicks. It is faster and repeatable, but needs solid knowledge.
- `describe` commands only read. Commands that change things start with run, create, delete or terminate.
- Plan previews changes, apply makes them. A second plan saying "No changes" means code and reality match.
- A template creates consistent configurations from one pattern. Data and template are separate so a site can be added without touching the template.
- Netmiko connects to devices over SSH so scripts can run commands and collect output. `device_type` tells it what kind of device (linux, cisco_ios).
- A playbook is a file with a list of tasks that describes the state I want. The second run said changed=0 because the target already matched.
- `--check` is a dry run. Its Terraform equivalent is `terraform plan`.

## Safety

No access keys were created. Terraform state, `.terraform`, `report.txt` and `.pem` keys never go to GitHub. All AWS resources were destroyed or terminated after each lab, and `scripts/cost_check.py` confirmed ALL CLEAR.
