{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Deny",
			"Action": [
				"ec2:RunInstances"
			],
			"Resource": [
				"arn:aws:ec2:*:*:instance/*"
			],
			"Condition": {
				"ForAnyValue:StringEquals": {
					"ec2:InstanceType": [
						"c5.large",
						"c5.xlarge",
						"c5.2xlarge",
						"m5.large",
						"m5.xlarge",
						"m5.2xlarge",
						"r5.large",
						"r5.xlarge",
						"r5.2xlarge",
						"t3a.large",
						"t3a.xlarge",
						"t3a.2xlarge",
						"t2.large",
						"t2.xlarge",
						"t2.2xlarge"
					]
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "s3:PutObject",
			"Resource": "arn:aws:s3:::*/*",
			"Condition": {
				"StringNotEquals": {
					"s3:x-amz-storage-class": [
						"STANDARD",
						"STANDARD_IA"
					]
				}
			}
		}
	]
}