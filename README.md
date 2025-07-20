# Face-Detection-attendance-by-Rekognition

├── frontend/
│   └── index.html  ← (the file you shared)
├── backend/
│   ├── generate-presigned-url.py or .js
│   └── detect-face.py or .js
├── README.md

🔧 System Architecture – Serverless Face Recognition Attendance System
This project implements a serverless attendance system using facial recognition, built entirely on AWS cloud services — without using a database.

🧱 Core Components:
Frontend (HTML + JavaScript)

Hosted on Amazon S3 and delivered globally via CloudFront

Lets users capture webcam images and trigger attendance

Amazon API Gateway

Serves as the REST API interface for:

Generating pre-signed S3 upload URLs

Triggering attendance marking logic

AWS Lambda Functions

Lightweight backend logic:

Generates secure pre-signed S3 URLs for uploading snapshots

Invokes Rekognition to identify faces from uploaded images

Returns the matched person info (stored in Rekognition Collection)

Amazon Rekognition

Facial recognition engine used to:

Compare uploaded images against a pre-indexed Collection

Identify employee based on face match confidence score

Amazon S3

Temporarily stores face snapshots uploaded from frontend

Also hosts the static frontend web application

Amazon CloudFront

Speeds up content delivery and acts as the public entry point for the web interface

Amazon CloudWatch

Monitors and logs Lambda function invocations and errors for debugging

🔄 Flow Overview
User accesses the frontend (HTML page via S3 + CloudFront)

Webcam is activated, user captures a face image

Frontend requests a pre-signed upload URL from API Gateway → Lambda

Lambda returns a signed S3 URL, and the frontend uploads the image

A second API call (or S3 event) triggers a Lambda

Lambda calls Rekognition to search for the face in an existing collection

Matched face (employee ID) is returned to the frontend and displayed as success/failure

(Optional) Logs are visible via CloudWatch for admins
