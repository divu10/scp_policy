import boto3

# Initialize the boto3 client
lambda_client = boto3.client('lambda', region_name='us-east-1')  # Change to your preferred region

def create_lambda_function():
    function_name = 'MyMinimalTestFunction'
    role_arn = 'arn:aws:iam::361769560345:role/service-role/abc-role-jv1ln4qv'  # Change to your IAM role ARN
    handler_name = 'lambda_function.lambda_handler'  # Entry point of the Lambda function
    runtime = 'python3.8'  # Choose the appropriate runtime

    # Read the ZIP file content
    with open('lamda.zip', 'rb') as zip_file:
        zip_content = zip_file.read()

    # Create Lambda function
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler_name,
        Code={
            'ZipFile': zip_content  # Upload ZIP file content
        },
        Description='A test Lambda function with ZIP file code',
        Timeout=15,  # Set timeout in seconds
        MemorySize=128,  # Set memory size in MB
        Tags={
            'Division': 'CD',  # Add tags if needed
            'Studio': 'Ajax',
            'Name'  : 'testing'
        }
    )

    # Print response
    print('Lambda function created successfully:')
    print(response)

if __name__ == '__main__':
    create_lambda_function()
