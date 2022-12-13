
'''
 boto3_create_unique_bucket.py: this code creates a unique s3 bucket.
'''
import boto3
import random
import string

def create_bucket_name(prefix):
    """ 
    This function generates a unique s3 bucket name.
    Parameters:
    prefix (str): user will provide a prefix of the bucket's name
    Returns:
    (str): returns a string as bucket's name that includes the prefix and 15 random characters at the end.
    """
    return (prefix + str(''.join(random.choices(string.ascii_lowercase, k=15))))

bucket_prefix = 'narcisse-bucket'

# body of the main
if __name__ == '__main__':
    try:
        # sending a request to interact with s3 API
        s3_client = boto3.client('s3')

        # creating s3 bucket in us-east-2
        response = s3_client.create_bucket(
            Bucket= create_bucket_name(bucket_prefix),
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-2',
            },
        )

        # printing response from s3 API
        print(response)

    except Exception as err:
        print ("Oops!  an error occured:", err)

