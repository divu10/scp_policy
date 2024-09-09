provider "aws"  {
region = "us-east-1"
}

locals {
#   tags = {}
  ORG  = "test-lambda"
  name = "${local.ORG}"

}


module "lambda_ec2_start" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "6.0.0"

  publish = true

  function_name = "${local.name}-ec2-start"
  description   = "Function to start EC2 instances."
  handler       = "main.lambda_handler"
  runtime       = "python3.8"

  source_path = "./${local.name}-ec2-start"

#   attach_cloudwatch_logs_policy = true
  attach_policy_json            = true
  policy_json                   = <<-EOT
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "EC2Start",
            "Effect": "Allow",
            "Action": [
              "ec2:Start*"
            ],
            "Resource": "*"
          }
        ]
      }
    EOT

tags = {

    Division = "CD"
    Studio = "Ajax"
}

}
