


import boto3
import logging

from botocore.exceptions import ClientError
import csv

# Setup Loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# constant global
FILE_NAME = 'ec2_report.csv'


def list_all_instances():
    # Call EC2 boto client
    ec2_client = boto3.client('ec2')

    # Retrieve all Ec2 instance in us-east-1 region
    response = ec2_client.describe_instances()

    # empty list
    lists = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # looking for the data needed
            server_name = instance['Tags'][0]['Value']
            instance_id = instance['InstanceId']
            image_id = instance['ImageId']
            instance_type = instance['InstanceType']

            # add our data to the list
            lists.append([server_name, instance_id, image_id, instance_type])
            
    
    return lists

def generate_excel_report(instances):


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
        Message="an Ec2 report {FILE_NAME} updated to S3 bucket", 
        Subject="notification email from your SNS ")
    return True

if __name__ == '__main__':

    logger.info(f'our list of server: {list_all_instances}')

    # retrieve data needed
    instances = list_all_instances()
    
    # past the instance list to the function
    generate_excel_report(instances)
    logger.info(f'Report: {FILE_NAME} has been generated succesfully!')

    # upload to s3 bucket
    upload_report_to_s3()
    logger.info(f'Report: {FILE_NAME} has been uploaded to S3 Bucket succesfully!')

    # call sns function
    send_an_sns_email()