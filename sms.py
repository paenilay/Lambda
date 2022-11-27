import boto3
import random
import json
from datetime import datetime,timedelta

#AWS_REGION = "your-region"
def lambda_handler(event, context):
    client = boto3.client('logs')

    startTime = datetime.now() - timedelta(minutes=15)
    startTime = int(startTime.strftime("%s")) * 1000
    
    endTime = datetime.now()
    endTime = int(endTime.strftime("%s")) * 1000
    
    EC2 = ["RunInstances", "StartInstances","StopInstances","TerminateInstances"]
    EC2SecurityGroups = ["AuthorizeSecurityGroupEgress","AuthorizeSecurityGroupIngress","RevokeSecurityGroupEgress","RevokeSecurityGroupIngress"]
    Route53 = ["ChangeResourceRecordSets","DeleteHealthCheck"]
    ECR = ["CreateRepository", "PutLifecyclePolicy","DeleteRepository","DeleteRepositoryPolicy"]
    EBS = ["CreateTags","CreateVolume","AssignVolume","AttachVolume","DeleteVolume","DescribeVolumes","DescribeVolumeStatus","DeleteSnapshot","DeregisterImage"]
    IAM = ["ConsoleLogin","CreateGroup","CreateLoginProfile","CreatePolicy","CreateUser","DeleteGroup","DeletePolicy","DeleteUser","RemoveUserFromGroup"]
    S3 = ["GetBucketAcl","CreateBucket","DeleteBucket","DeleteBucketCors","DeleteBucketLifecycle","DeleteBucketPolicy","DeleteBucketReplication","DeleteBucketTagging","PutBucketAcl","PutBucketCors","PutBucketLifecycle","PutBucketLogging","PutBucketNotification","PutBucketPolicy","PutBucketReplication","PutBucketRequestPayment","PutBucketTagging","PutBucketVersioning","PutBucketWebsite"]
    VPC = ["CreateNatGateway","CreateKeyPair","CreateNetworkAcl","CreateNetworkInterface","CreateRoute","CreateSecurityGroup","CreateVpc","CreateVpcEndpoint","CreateVpnGateway"]
    
    #Filter the most recent logstream
    response = client.describe_log_streams(
    logGroupName='your-cloudtrail-logs',
    orderBy='LastEventTime',
    descending=False
    
)
