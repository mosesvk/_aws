import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crud-users')

def lambda_handler(event, context):
    method = event.get('httpMethod')
    body = json.loads(event.get('body') or '{}')
    path_params = event.get('pathParameters') or {}
    user_id = path_params.get('userId')

    try:
        if method == 'POST':
            table.put_item(Item=body)
            return response(201, {'message': 'Created', 'item': body})

        if method == 'GET' and user_id:
            result = table.get_item(Key={'userId': user_id})
            return response(200, result.get('Item', {}))

        if method == 'GET':
            result = table.scan()
            return response(200, result.get('Items', []))

        if method == 'PUT':
            table.update_item(
                Key={'userId': user_id},
                UpdateExpression='set #n = :n',
                ExpressionAttributeNames={'#n': 'name'},
                ExpressionAttributeValues={':n': body.get('name')}
            )
            return response(200, {'message': 'Updated'})

        if method == 'DELETE':
            table.delete_item(Key={'userId': user_id})
            return response(200, {'message': 'Deleted'})

    except Exception as e:
        return response(500, {'error': str(e)})


def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }