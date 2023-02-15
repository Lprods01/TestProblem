import boto3
import uuid
import json
from botocore.exceptions import ClientError
from mimetypes import guess_extension

def generate_presigned_url(extension, bucket = 'trs-public-assets-5n4jhbxkl409vnfk', expires_in = 1200):
    key = uuid.uuid1().hex + extension
    try:
        res = boto3.client('s3').generate_presigned_post(
            Bucket = bucket,
            Key = key,
            ExpiresIn=expires_in
        )
    except ClientError:
        raise
    print(res)
    return {'res': res, 'imageURI': 'https://trs-public-assets-5n4jhbxkl409vnfk.s3-us-west-2.amazonaws.com/' + key}

def createUrl(event, context):
    try:   
        ret = generate_presigned_url(extension = guess_extension(event["queryStringParameters"]['Content-Type']))
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 404,
            'body': json.dumps("error")
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(ret)
        }