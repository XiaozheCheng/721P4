import csv

s3 = boto3.client('s3')

def lambda_handler(event, context):
  
    key = '721p4.csv'
    
    response = s3.get_object(Bucket='my-bucket', Key=key)
    content = response['Body'].read().decode('utf-8')
    
    lines = content.split('\n')
    for line in csv.reader(lines):
        print(line)



