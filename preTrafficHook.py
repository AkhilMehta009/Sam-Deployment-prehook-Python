import json
import boto3
import os


def lambda_handler(event, context):
    deploymentId = event["DeploymentId"]
    lifecycleEventHookExecutionId = event["LifecycleEventHookExecutionId"]
    client = boto3.client("lambda", region_name="us-east-2")
    codeclient = boto3.client("codedeploy")
    payload = {"message": "Hi, you have been invoked."}
    funname = os.environ["NewVersion"]
    status = "Failed"
    resp = client.invoke(
        FunctionName=funname,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    dic = json.loads(resp["Payload"].read().decode("utf-8"))

    dic = json.loads(dic["body"])
    # print(dic["status"]==200)

    if dic["status"] == 200:
        status = "Succeeded"
    else:
        status = "Failed"

    _ = codeclient.put_lifecycle_event_hook_execution_status(
        deploymentId=deploymentId,
        lifecycleEventHookExecutionId=lifecycleEventHookExecutionId,
        status=status,
    )
