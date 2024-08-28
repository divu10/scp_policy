# SCP Policy

This repository includes an SCP policy for the AWS root account, along with methods to test it using Terraform, Boto3 Python API, and the AWS Console.

# AWS Root Account SCP Policy

## Description

This repository provides an SCP (Service Control Policy) that can be applied at the AWS root account level. It includes various methods to test the policy, such as using Terraform, the Boto3 Python API, and the AWS Console.

## Table of Contents

- [Prerequisites](#prerequisites)
- [SCP Policy](#scp-policy)
- [Testing Methods](#testing-methods)
  - [Using Terraform](#using-terraform)
  - [Using Boto3 Python API](#using-boto3-python-api)
  - [Using AWS Console](#using-aws-console)
- [Note](#note)


## Prerequisites

- AWS account with appropriate permissions
- Terraform installed on your local machine
- Python with Boto3 installed
- Access to the AWS Management Console

## SCP Policy

The SCP policy provided in this repository is designed to enforce specific restrictions at the root level of your AWS organization. You can customize the policy according to your requirements.

## Testing Methods

### Using Terraform Test Case 

1. Clone the repository.
2. Navigate to the `terraform/` directory.
3. Run `terraform init` to initialize the Terraform environment.
4. Run `terraform apply` to test the SCP policy.

### Using Boto3 Python API Test Case

1. Clone the repository.
2. Navigate to the `boto3/` directory.
3. Update the `scp_policy.py` script with your policy details.
4. Run the script using `python scp_policy.py` to test the SCP policy.

### Using AWS Console 

1. Log in to the AWS Management Console.
2. Navigate to the AWS Organizations section.
3. Select the root account where you want to apply the SCP.
4. Create a new SCP policy by copying the contents of the `scp_policy.json` file.
5. Attach the policy to the desired OU or account.

## Note

- Ensure that you thoroughly test the SCP policy in a non-production environment before applying it to your production account. Misconfigurations can lead to unintended access restrictions, potentially disrupting your AWS services.
- Each policy directory includes its own test cases, which can be executed using various methods such as Terraform, the Boto3 Python API, etc.

## Made with Love

❤️ This project was made with love to help make your AWS management easier and more secure.
