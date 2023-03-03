
import boto3
import logging
from botocore.exceptions import ClientError
import csv

# Setup Loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# constant global
FILE_NAME = 'ec2_report.csv'


# scan and retrieve all stopped Ec2 instances in us-east-1 region 
def list_all_instances():
    # Call EC2 boto client
    ec2_client = boto3.client('ec2')

    # filter and return only stopped Ec2 instances in us-east-1 region 
    response = ec2_client.describe_instances(
        Filters=[
    {
        'Name': 'instance-state-name',
        'Values': [
            'stopped'
            
        ]
    },
        ]
    )

    # empty list
    lists = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # looking for the data needed
            server_name = instance['Tags'][0]['Value']
            instance_id = instance['InstanceId']
            image_id = instance['ImageId']
            volume_id = instance['BlockDeviceMappings'][0]['Ebs']['VolumeId']
            instance_type = instance['InstanceType']

            # add our data to the list
            lists.append([server_name, instance_id, image_id, volume_id, instance_type])
    return lists

# Create an EBS snapshot of that EC2
def ebs_snapshot_stopped_ec2():

#Creating a Snapshot from an EBS volume (with waiter)
    AWS_REGION = "us-east-1"
    ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
     # empty list
    snapshot_lists = []

    stopped_ec2 = list_all_instances()
    for m in stopped_ec2:
        # create EBS snapshots 
        snapshot = ec2_resource.create_snapshot(
            VolumeId= m[3],
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'boto3-created-EBS-snapshot'
                             },
                        ]
                 },
             ]
        )
        snapshot.wait_until_completed()
        print(f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')

        snapshot_lists.append(snapshot.id)
    return snapshot_lists

# Terminate stopped ec2 instances
def terminate_stopped_ec2():

# Creating a client connection with AWS EC2 
    ec2_clean = boto3.client('ec2')
# Use response = ec2.start_instances( if you need to Start the Machine
# Use response = ec2.terminate_instances( if you need to terminate the Machine

# terminating the instance using terminate_instances.
    for inst in list_all_instances():
        response = ec2_clean.terminate_instances(
	        InstanceIds=[
            inst[1] #'i-03e3d79d5def39c75',
        ],
    )

    print('all stopped instances were terminated successfully')

# Generate a csv report
def generate_csv_report(instances):


    ''' Generate an Excel Report

    :param instances: List of instances

    :return: True if file was generated, else False
    '''

    # csv header
    header = ['Server Name', 'Instance ID', 'Ami ID', 'Instance Type']
    try:
        with open(FILE_NAME, 'w',  newline='') as file:
            write = csv.writer(file) # start writing to CSV file
            write.writerows(header)
            write.writerows(instances)
    except FileNotFoundError as error:
        logger.error('File does not exixt: {error}')
        return False
    return True


# Upload the csv report to s3 bucket
def upload_report_to_s3():

    ''' Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False

    '''
    # Bucket name
    narcisse_bucket = 'statebucket6655'
    
    # calling the s3 client
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(FILE_NAME, narcisse_bucket, 'mimi.csv')
    except ClientError as e:
        logging.error(e)
        return False
    return True

def send_an_sns_email():

    ''' Send an Email using SNS to subscriber

    :param Name: topic name to create
    :param TopicArn: Amazon arn of the created topic
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False

    '''

    # calling the client
    sns = boto3.client("sns")

    # create a topic
    response = sns.create_topic(Name="report_email")
    print(response)
    topic_arn = response["TopicArn"]

    # Create email subscription
    response = sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint="narherve@yahoo.com")
    subscription_arn = response["SubscriptionArn"]

    print(topic_arn)

    print(subscription_arn)

    # Publish to topic
    sns.publish(TopicArn=topic_arn, 
        Message="an Ec2 report {FILE_NAME} was updated to S3 bucket", 
        Subject="notification email from your SNS ")
    return True

if __name__ == '__main__':

    logger.info(f'our list of server: {list_all_instances}')

    # retrieve data needed
    instances = list_all_instances()
    
    # create ebs snapshots
    snapshots = ebs_snapshot_stopped_ec2()

    print(f"the list of created snapshots is :{snapshots}")

    # past the instance list to the function
    generate_csv_report(instances)
    logger.info(f'Report: {FILE_NAME} has been generated succesfully!')

    # terminate all instances
    terminate_stopped_ec2()

    # upload to s3 bucket
    upload_report_to_s3()
    logger.info(f'Report: {FILE_NAME} has been uploaded to S3 Bucket succesfully!')

    # call sns function
    send_an_sns_email()