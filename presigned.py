import json
import boto3
import uuid
import os

# Initialize S3 client
s3_client = boto3.client('s3')

# Set your S3 bucket name from environment variable or default
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'face-frontend-bucket')

def lambda_handler(event, context):
    try:
        # Parse the incoming JSON body
        body = json.loads(event['body'])

        file_name = body.get('fileName')
        file_type = body.get('fileType')

        if not file_name or not file_type:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'fileName and fileType are required'})
            }

        # Generate a unique key for the uploaded file in S3
        unique_file_key = f'attendance-uploads/{uuid.uuid4()}_{file_name}'

        # Generate the pre-signed URL for uploading the file to S3
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': unique_file_key,
                'ContentType': file_type
            },
            ExpiresIn=300  # URL will be valid for 5 minutes
        )

        # Return the pre-signed URL and file key
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps({
                'uploadUrl': presigned_url,
                'fileKey': unique_file_key
            })
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
