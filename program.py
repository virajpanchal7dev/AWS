import boto3
import json

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print("Output")
    print(response)

create_user("test-iam-user")

def list_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response["Users"]:
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

list_users()

def update_user(old_user_name, new_user_name):
    iam = boto3.client('iam')
    # Update a user name
    response = iam.update_user(
        UserName=old_user_name,
        NewUserName=new_user_name
    )
    print(response)

update_user("test-iam-user", "sample-iam-user")
list_users()

def list_policies():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_policies')
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")

list_policies()


def create_iam_policy():
    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:GetItem",
                    "dynamodb:Scan",
                ],
                "Resource": "*"
            }
        ]
    }
    response = iam.create_policy(
        PolicyName='testDynamoDBPolicy',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

create_iam_policy()
list_policies()

def attach_user_policy(policy_arn, username):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

attach_user_policy(policy_arn="arn:aws:iam::851799637821:policy/testDynamoDBPolicy", username="sample-iam-user")

def create_group(group_name):
  iam = boto3.client('iam') # IAM low level client object
  iam.create_group(GroupName=group_name)

create_group("my-test-group")

def add_user_to_group(username, group_name):
    iam = boto3.client('iam') # IAM low level client object
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )
    print(response)

add_user_to_group("sample-iam-user", "my-test-group")


def attach_group_policy(policy_arn, group_name):
    iam = boto3.client("iam")
    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    print(response)

attach_group_policy(policy_arn="arn:aws:iam::851799637821:policy/testDynamoDBPolicy", group_name="my-test-group")










