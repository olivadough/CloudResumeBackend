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
            'Name': 'Count'
        },
        UpdateExpression='SET Count = Count + :val',
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnConsumedCapacity= 'NONE',
        ReturnItemCollectionMetrics='NONE',
        
        ReturnValues= 'ALL_NEW'
    )
    return {
      'statusCode': 200,
      'body': responseUpdate['Count']
    }