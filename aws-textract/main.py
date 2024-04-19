import os
from module.aws.aws import aws
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()

if __name__ == "__main__":

    AWS_REGION = os.getenv('AWS_REGION')
    AWS_PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')
    AWS_BUCKET = os.getenv('AWS_BUCKET')

    FILE_BUCKET = 'crlve.pdf'
    
    aws.awsTextract(AWS_PROFILE_NAME, AWS_REGION, AWS_BUCKET, FILE_BUCKET)