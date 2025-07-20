📁 Project Structure
bash
Copy
Edit
face-detection-attendance-by-rekognition/
      1. frontend/  └── index.html                  # Web interface (camera access + upload)
      2. backend/
             generate-presigned-url.py  # Lambda: generates signed S3 upload URLs
            rekognition.json             # Lambda: calls Rekognition to match face
      3. README.md                      # Project documentation

🏗️ System Architecture
This system uses a serverless architecture built entirely on AWS.

🔧 Core Components
Frontend (HTML + JavaScript)
Hosted on Amazon S3 and delivered via CloudFront. It captures webcam images and uploads them to S3 using pre-signed URLs.

1. Amazon S3
      Stores the static website (index.html) and uploaded face images.

2. Amazon CloudFront
      Distributes the web interface globally with low latency.

3. Amazon API Gateway
      Serves as the REST API layer to access Lambda functions securely.

4. AWS Lambda
      Handles the backend logic:

5. Generates pre-signed URLs for secure S3 upload
      Invokes Rekognition for facial comparison

6. Amazon Rekognition
      Compares uploaded faces against a pre-indexed Rekognition Collection and returns the matched user.

7. Amazon CloudWatch
      Logs Lambda invocations and errors for monitoring and debugging.

🔄 Workflow (How It Works)
1. User accesses the frontend (served via S3 + CloudFront).
2. The webcam activates and captures a face image.
3. Frontend requests a pre-signed URL from API Gateway → Lambda.
4. Lambda returns the signed URL; the image is uploaded to S3.
5. A second API call (or automatic trigger) invokes another Lambda function.
6. This Lambda function calls Rekognition to compare the face with stored images in the Collection.
7. The matched result (Employee ID or failure message) is returned to the frontend.

🚀 Deployment Steps

✅ You need an AWS account with appropriate IAM permissions.
Step-1. Create an S3 Bucket for hosting the frontend and storing uploads.
Step-2 Create a Rekognition Collection and index known employee face images.
Step-3 Deploy two Lambda functions:
       generate-presigned-url.py
      rekognition.json
Step-4 Set up API Gateway to connect the frontend to your Lambda functions.
Step-5 Enable CORS for both the S3 bucket and API Gateway.
Step-6 Upload index.html to the S3 bucket and connect it to CloudFront.

📸 Use Case Example
The employee visits the web app via browser.
Captures their face using the webcam.
Face is compared with existing faces in the Rekognition Collection.
Attendance is marked automatically if a match is found.
