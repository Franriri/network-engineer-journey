# Terraform VPC lab

Builds `tf-lab-vpc` (10.1.0.0/16) with a public and a private subnet, an Internet Gateway, a route table and a security group.
All resources are free. The code was written with Claude. I applied, verified and destroyed it.

## Run in AWS CloudShell

CloudShell has 1 GB of persistent storage and the AWS provider is large, so keep Terraform's data in /tmp:

```
mkdir -p /tmp/tf-data /tmp/tf-plugin-cache
export TF_DATA_DIR=/tmp/tf-data
export TF_PLUGIN_CACHE_DIR=/tmp/tf-plugin-cache
terraform init
terraform plan        # expect: Plan: 7 to add
terraform apply       # type yes
terraform plan        # expect: No changes
terraform destroy     # type yes, always clean up
```

## Safety

- Never commit `terraform.tfstate` or the `.terraform` folder.
- Only `main.tf` belongs in this repository.
