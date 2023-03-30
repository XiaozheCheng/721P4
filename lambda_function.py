
import json

def lambda_handler(event, context):

    name = event['name']
    age = event['age']

 
    message = f"Hello, {name}! You are {age} years old."

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

