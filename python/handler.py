import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visitors')
    response = table.update_item(
        Key={
            'Mainkey': 'iou'
        },
        UpdateExpression='ADD Visits :increment',
        ExpressionAttributeValues={
            ':increment': 1
        },
        ReturnValues= 'ALL_NEW'
    )

    return {
      'statusCode': 200,
      'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
      'body': int(response['Attributes']['Visits'])
    }