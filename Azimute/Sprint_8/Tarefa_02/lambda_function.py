import boto3
import requests
import json
from datetime import datetime

bucket_name = 'data-lake-do-fabricio'
raw_prefix = 'Raw/API/TMDB/JSON'

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

def lambda_handler(event, context):
    
    api_key = "cb80207881bf04ccb9a3258c1f1281e1"
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"
    
    
    s3 = boto3.client('s3')
    
    
    response = requests.get(url)
    data = response.json()
    
    file_name = f'{year}{month}{day}_tmdb.json'
    file_path = f'{raw_prefix}/{year}/{month}/{day}/{file_name}'
    s3.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=file_path)
    
    return {
        'statusCode': 200,
        'body': 'Dados do TMDB salvos com sucesso no S3!'
    }




