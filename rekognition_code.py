import boto3
import os

rekognition = boto3.client('rekognition')

# Set your collection ID and S3 bucket info
COLLECTION_ID = 'employee-collection'   # Replace with your actual collection name
S3_BUCKET = 'employee-bucket-v1-face-attendance'      # Replace with your S3 bucket name
REFERENCE_DIR = 'stored_image'      # S3 folder where images are stored

# You can also move this to a config file or DynamoDB if needed
person_files = {
    'Lekhana_vemuri': 'Lekhana_vemuri.jpg',
    'priti_Nalgiri' : 'priti_Nalgiri.jpg',
}

def lambda_handler(event, context):
    for name, filename in person_files.items():
        s3_key = f"{REFERENCE_DIR}/{filename}"

        try:
            response = rekognition.index_faces(
                CollectionId=COLLECTION_ID,
                Image={
                    'S3Object': {
                        'Bucket': S3_BUCKET,
                        'Name': s3_key
                    }
                },
                ExternalImageId=name,
                DetectionAttributes=['DEFAULT']
            )

            face_records = response.get('FaceRecords', [])
            if face_records:
                print(f"Indexed {name}: FaceId = {face_records[0]['Face']['FaceId']}")
            else:
                print(f"Failed to index {name} (no face detected)")

        except Exception as e:
            print(f"Error indexing {name}: {e}")
