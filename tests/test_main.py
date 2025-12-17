import boto3

def test_aws_connection():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()

    print("✅ Connected to AWS!")
    print(f"Account ID: {identity['Account']}")
    print(f"User/Role ARN: {identity['Arn']}")

if __name__ == "__main__":
    test_aws_connection()
