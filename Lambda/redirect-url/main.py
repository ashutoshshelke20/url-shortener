import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener')

def lambda_handler(event, context):
    raw_path = event.get("path", "")
    short_code = raw_path.lstrip("/")  # Remove the leading '/'
    
    print(f"shortcode {short_code}")
    
    result = table.get_item(Key={'shortCode': short_code})
    item = result.get('Item')

    if not item:
        return {'statusCode': 404, 'body': 'Short URL not found'}

    return {
        'statusCode': 301,
        'headers': {'Location': item['longUrl']}
    }
