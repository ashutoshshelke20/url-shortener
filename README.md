# 🔗 Serverless URL Shortener using AWS and Python

This project is a serverless URL shortener built using:
- AWS Lambda (Python)
- API Gateway
- DynamoDB
- (Optional) S3 Static Hosting

## 🚀 Features
- Generate short URLs using random IDs
- Store original/short mappings in DynamoDB
- Redirect using GET requests
- Deployed via API Gateway and Lambda

## 🛠 Architecture
1. POST `/shorten` – accepts JSON with original URL
2. GET `/{short_id}` – redirects to original URL
3. DynamoDB stores mapping of `shortId` → `originalUrl`
4. Lambda handles backend logic

## 🧪 Sample Request (POST)
```bash
curl -X POST https://your-api-id.amazonaws.com/shorten \
 -H "Content-Type: application/json" \
 -d '{"url": "https://example.com"}'

