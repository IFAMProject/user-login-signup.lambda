import json
import boto3
import os
from aws_lambda_typing import events, context_
from typing import Dict, Any

def handler(event: event.APIGatewayProxyEventV2, context: context_.Context) -> Dict[str, any]:
	print(event)
	print(context)

	path = event.get("rawPath", "")
	body = json.loads(event.get("body") or "{}")

	print(path)
	print(body)