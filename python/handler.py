import boto3
from boto3.dynamodb.conditions import Key, Attr

def placeholder(event, context):
            return {'body': 'Hello World! #2', 'statusCode': 200}

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NumberOfVisitors')
    responseUpdate = table.update_item(
        Key={
            'Name': 'Count',
            'Type': 'Number' 
        },
        UpdateExpression="SET Count = Count + :val",
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues="Count"
    )
    
    response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
    )

    return {
      'statusCode': 200,
      'body': response
    }