import boto3

def handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NumberOfVisitors')
    

    return {'body': table, 'statusCode': 200}

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NumberOfVisitors')
    responseUpdate = table.update_item(
        Key={
            'Name': 'NumberOfVisitors'
        },
        UpdateExpression="SET Count = Count + :val",
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues= 'UPDATED_NEW'
    )
    return {
      'statusCode': 200,
      'body': responseUpdate['Count']
    }