import boto3

aws_mang_console=boto3.session.Session(profile_name='xxxxx')
s3_console=aws_mang_console.resource('s3')

for bucket in s3_console.buckets.all():
    print (bucket.name)
