# Face-Detection-attendance-by-Rekognition

face-detection-attendance-by-rekognition/
├── frontend/
│   └── index.html                  # Web interface (camera access + upload)
├── backend/
│   ├── generate-presigned-url.py  # Lambda: generates signed S3 upload URLs
│   └── detect-face.py             # Lambda: calls Rekognition to match face
├── README.md                      # Project documentation


🔧 System Architecture – Serverless Face Recognition Attendance System
This project implements a serverless attendance system using facial recognition, built entirely on AWS cloud services — without using a database.

🧱 Core Components:
Frontend (HTML + JavaScript)

1. Hosted on Amazon S3 and delivered globally via CloudFront

      Lets users capture webcam images and trigger attendance

2. Amazon API Gateway

    Serves as the REST API interface for:

    Generating pre-signed S3 upload URLs

    Triggering attendance marking logic

3. AWS Lambda Functions

    Lightweight backend logic:

    Generates secure pre-signed S3 URLs for uploading snapshots

    Invokes Rekognition to identify faces from uploaded images

    Returns the matched person info (stored in Rekognition Collection)

4. Amazon Rekognition

    Facial recognition engine used to:

    Compare uploaded images against a pre-indexed Collection

    Identify employee based on face match confidence score

5. Amazon S3

    Temporarily stores face snapshots uploaded from frontend

    Also hosts the static frontend web application

6. Amazon CloudFront

    Speeds up content delivery and acts as the public entry point for the web interface

7. Amazon CloudWatch

     Monitors and logs Lambda function invocations and errors for debugging

🔄 Flow Overview
User accesses the frontend (HTML page via S3 + CloudFront)

    Webcam is activated, user captures a face image

    Frontend requests a pre-signed upload URL from API Gateway → Lambda

    Lambda returns a signed S3 URL, and the frontend uploads the image

    A second S3 event triggers a Lambda

    Lambda calls Rekognition to search for the face in an existing collection

    Matched face (employee ID) is returned to the frontend and displayed as attendance success


