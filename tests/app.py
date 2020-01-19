import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]

    # print("Bucket List: %s" % buckets)

    # print("Status result ",context)
    return {
        "statusCode": 200,
        "body": json.dumps({"List": buckets, "event": event, "status": 300}),
    }
