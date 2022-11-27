import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    ###Get All Volumes in the current account.
    allVol = ec2.describe_volumes()
    
    ###These Volumes are to be snapshot
    snapShotList = ["vol-xxxxx"]
    
    ###Show all volumes in the current account
    for volume in allVol['Volumes']:
        
        print("VolumeId" +":"+ volume["VolumeId"])
        print("State" +":"+ volume["State"])
        print("AvailabilityZone" +":"+ volume["AvailabilityZone"])
        
        print("\n Now we will filter out the volumes to take snapshot")
        
        
        ###Filter the volume to take snapshot
        if volume["VolumeId"] in snapShotList:
            print(volume["VolumeId"] + "need to take snapshot")
            
            
            #Create Snapshot
            result = ec2.create_snapshot(VolumeId=volume['VolumeId'],Description="Lambda Snapshot")
            
            # Get snapshot resource
            ec2resource = boto3.resource('ec2')
            snapshot = ec2resource.Snapshot(result['SnapshotId'])
        
            # Find name tag for volume
            if 'Tags' in volume:
                for tags in volume['Tags']:
                    if tags["Key"] == 'Name':
                        volumename = tags["Value"]
            else:
                volumename = 'N/A'
            
            # Add volume name to snapshot for easier identification
            snapshot.create_tags(Tags=[{'Key': 'Name','Value': volumename}])
