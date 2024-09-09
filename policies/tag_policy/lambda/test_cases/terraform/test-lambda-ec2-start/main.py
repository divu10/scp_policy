import boto3

region = 'us-east-1'
instances = ['i-04099edf13841a76f'] #TODO change after creation.
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
  ec2.start_instances(InstanceIds=instances)
  print("Started instances: " + str(instances))
