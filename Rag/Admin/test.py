import boto3

input_text = "Hello, world!"

bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock_client.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    contentType="application/json",
    body='{"inputText": "Hello, world!"}'
)


print(response['body'].read().decode('utf-8'))
