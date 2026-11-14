# Terraform VPC lab (written with Claude, applied and destroyed by Fran)
# Builds a small VPC: public and private subnet, Internet Gateway, route table, security group.
# All resources are free. Always run "terraform destroy" when the lab ends.
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-2"
}

variable "name_prefix" {
  type    = string
  default = "tf-lab"
}

locals {
  common_tags = {
    Project   = "network-journey"
    ManagedBy = "terraform"
  }
}

resource "aws_vpc" "main" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_hostnames = true
  tags = merge(local.common_tags, { Name = "${var.name_prefix}-vpc" })
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.1.1.0/24"
  availability_zone       = "ap-southeast-2a"
  map_public_ip_on_launch = true
  tags = merge(local.common_tags, { Name = "${var.name_prefix}-public-subnet" })
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.1.2.0/24"
  availability_zone = "ap-southeast-2a"
  tags = merge(local.common_tags, { Name = "${var.name_prefix}-private-subnet" })
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags   = merge(local.common_tags, { Name = "${var.name_prefix}-igw" })
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = merge(local.common_tags, { Name = "${var.name_prefix}-public-rt" })
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "public" {
  name        = "${var.name_prefix}-public-sg"
  description = "Lab security group with no inbound rules"
  vpc_id      = aws_vpc.main.id
  tags        = merge(local.common_tags, { Name = "${var.name_prefix}-public-sg" })
}

output "vpc_id" {
  value = aws_vpc.main.id
}
