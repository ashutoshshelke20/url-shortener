# Serverless URL Shortener App (AWS + Python)

A serverless application that converts long URLs into short ones using AWS.

## 🔧 Tech Stack
- AWS Lambda (Python)
- API Gateway
- DynamoDB
- S3 (Frontend)
- EC2 (Git Deployment)

## 🌐 Features
- Shorten long URLs using a REST API
- Redirect to the original long URL via short code
- Static website frontend hosted on S3

## 🛠️ Deployment Steps

1. Create a DynamoDB table: `UrlShortener` with primary key `shortCode`
2. Create two Lambda functions:
   - `shorten-url` (POST) — generates short URL and stores it
   - `redirect-url` (GET) — redirects to the long URL
3. Setup API Gateway:
   - POST `/shorten`
   - GET `/{shortcode}`
4. Upload the frontend (HTML/JS) to S3 and enable static hosting


## 🧪 Sample Request (POST)
```bash
curl -X POST "https://of707r5sw0.execute-api.eu-north-1.amazonaws.com/prod/shorten-url" -d "{\"longUrl\" : \"https://www.google.com\"}"
```

