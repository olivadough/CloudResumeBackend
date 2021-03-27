import boto3

def handler2(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visitors')
    

    return {'body': table, 'statusCode': 200}

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visitors')
    response = table.update_item(
        Key={
            'Mainkey': 'iou'
        },
        UpdateExpression='ADD Visits :1',
        ReturnValues= 'ALL_NEW'
    )
    return {
      'statusCode': 200,
      'body': response
    }