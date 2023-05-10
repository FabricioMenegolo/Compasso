import boto3
import requests
import json
from datetime import datetime

s3 = boto3.resource('s3')
bucket_name = 'data-lake-do-fabricio'
raw_prefix = 'Raw/Local/JSON'

def lambda_handler(event, context):
    
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    
    movies_url = f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_keywords=285442'
    series_url = f'https://api.themoviedb.org/3/discover/tv?include_null_first_air_dates=false&sort_by=popularity.desc&with_genres=16%252C10759%252C10765&with_keywords=210024%252C13141&with_original_language=ja'

    headers = {
        "accept": "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjgwMjA3ODgxYmYwNGNjYjlhMzI1OGMxZjEyODFlMSIsInN1YiI6IjY0NTNmNTRmODdhMjdhMDE1NDMyNWM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9tYrFHogchw7N6x09PQ4zJTeTz8wGKOqn5dy6LYVQgw"
    }
    
    # Requisição na API para obter dados dos filmes
    response = requests.get(movies_url, headers=headers)
    data = json.loads(response.text)
    movies = data.get('results')
    print(movies)
    
    # Salvando dados dos filmes em arquivo JSON no S3
    movies_file = f'movies_{now.strftime("%Y%m%d_%H%M%S")}.json'
    movies_path = f'{raw_prefix}/Movies/{year}/{month}/{day}/{movies_file}'
    s3.Object(bucket_name, movies_path).put(Body=json.dumps(movies))
    
    # Requisição na API para obter dados das séries de TV
    response = requests.get(series_url, headers=headers)
    data = json.loads(response.text)
    series = data.get('results')
    print(series)
    
    # Salvando dados das séries em arquivo JSON no S3
    series_file = f'series_{now.strftime("%Y%m%d_%H%M%S")}.json'
    series_path = f'{raw_prefix}/Series/{year}/{month}/{day}/{series_file}'
    s3.Object(bucket_name, series_path).put(Body=json.dumps(series))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos com sucesso no S3!')
    }

