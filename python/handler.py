import boto3

def handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NumberOfVisitors')
    

    return {'body': table, 'statusCode': 200}

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NumberOfVisitors')
    response = table.update_item(
        Key={
            'Name': 'iou'
        },
        UpdateExpression='SET Visits = Visits + :val',
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues= 'ALL_NEW'
    )
    return {
      'statusCode': 200,
      'body': response
    }