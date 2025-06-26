import json
import boto3
import string
import random
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener')

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body.get('longUrl')

    if not long_url:
        return {'statusCode': 400, 'body': 'Missing longUrl'}

    short_code = generate_code()
    table.put_item(Item={
        'shortCode': short_code,
        'longUrl': long_url,
        'createdAt': int(time.time())
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'shortUrl': f'https://of707r5sw0.execute-api.eu-north-1.amazonaws.com/prod/{short_code}'}),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }
