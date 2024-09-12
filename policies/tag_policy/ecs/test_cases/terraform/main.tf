provider "aws" {
  region = "us-east-1"
}

module "ecs_cluster" {
  source = "cloudposse/ecs-cluster/aws"

  namespace = "eg"
  name      = "example"

  container_insights_enabled      = true
  capacity_providers_fargate      = true

  tags = {
    Division = "CD"
    Studio   = "Ajax"
    Name = "test"
  }
}