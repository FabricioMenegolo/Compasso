import boto3
import requests
import json
from datetime import datetime

s3 = boto3.resource('s3')
bucket_name = 'data-lake-do-fabricio'
raw_prefix = 'Raw/TMDB/JSON'


api_key = "cb80207881bf04ccb9a3258c1f1281e1"
movie_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"
tv_url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=pt-BR"

    # Configuração das informações de data
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

    # Faz a requisição dos dados de filmes
response = requests.get(movie_url)
if response.status_code == 200:
    movies_data = response.json()
    movies_file = f"movies_{year}{month}{day}.json"
    movies_path = f"{raw_prefix}/Movies/{year}/{month}/{day}/{movies_file}"
    #s3.Object(bucket_name, movies_path).put(Body=json.dumps(movies_data))

    # Faz a requisição dos dados de séries
response = requests.get(tv_url)
if response.status_code == 200:
    series_data = response.json()
    series_file = f"series_{year}{month}{day}.json"
    series_path = f"{raw_prefix}/Series/{year}/{month}/{day}/{series_file}"
    #s3.Object(bucket_name, series_path).put(Body=json.dumps(series_data))