# Module 4: Network Automation and Infrastructure as Code

**Analogy:** clicking in the console is cooking from memory. Automation is a recipe that gives the same meal every time.

## Key terms

| Term | Meaning |
|---|---|
| CLI | Controlling AWS with typed commands |
| API / SDK (boto3) | The menu AWS offers to programs / the Python library that uses it |
| IaC | Infrastructure as Code: describe infrastructure in files |
| Terraform | Free IaC tool: write what you want, it builds it |
| Template (Jinja2) | A form letter with blanks that data fills in |

## Lab 1: AWS CLI in CloudShell (read-only)

- `aws ec2 describe-vpcs --output table`, then `--query` to choose columns.
- A pager can open long output: press `q` to leave, or run `export AWS_PAGER=""`.
- Cost-safety checks by command: instances, Elastic IPs, NAT gateways, volumes.
- `describe` commands only read. Commands that change things start with run, create, delete or terminate.

## Lab 2: Python cost-safety checker

[`scripts/cost_check.py`](../scripts/cost_check.py) runs the four checks at once with boto3 and prints one report (ALL CLEAR when nothing can cost money). Written with AI assistance. I ran it and checked it against my manual checks.

## Lab 3: Terraform

[`labs/terraform`](../labs/terraform/) builds a VPC from code: init, plan (7 to add), apply, verify with the AWS CLI, plan again (No changes), destroy.
Problem solved: CloudShell home storage is 1 GB and the AWS provider is large, so Terraform's data moved to /tmp.

## Lab 4: Config templates

[`labs/network-automation`](../labs/network-automation/) generates three router configurations from one Jinja2 template. I tested the BR1 config in Packet Tracer: interface up/up and 4 of 4 ping replies.

## Quick check (polished)

- A template creates consistent configurations from one pattern, faster and without typing mistakes.
- `{{ }}` marks blanks that data fills in.
- Data and template are separate so that I can add sites without changing the template, and change the standard once for all sites.
- Plan previews changes. Apply makes them. A second plan saying "No changes" means the code and the real infrastructure match.

## Safety

No access keys were created. Terraform state and `.terraform` never go to GitHub. All AWS resources were destroyed after each lab.
