import boto3
aws_console=boto3.session.Session(profile_name="xxxxxx")
iam_console=aws_console.resource('iam')

for indv_user in iam_console.users.all():
    print(indv_user.name)
