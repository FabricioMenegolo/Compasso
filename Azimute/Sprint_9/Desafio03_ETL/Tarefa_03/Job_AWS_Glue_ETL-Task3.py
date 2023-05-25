import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, substring, when, size
from datetime import datetime


sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


# Define os caminhos dos arquivos no S3
path1 = "s3://data-lake-do-fabricio/Raw/Local/CSV/Movies/2023/05/02/"
path2 = "s3://data-lake-do-fabricio/Raw/Local/CSV/Series/2023/05/02/"
path3 = "s3://data-lake-do-fabricio/Raw/TMDB/JSON/Movies/2023/05/24/"
path4 = "s3://data-lake-do-fabricio/Raw/TMDB/JSON/Series/2023/05/24/"

# Carrega os DataFrames
df_movies_IMDB = spark.read.option("delimiter", "|").csv(path1 + 'movies.csv', header=True)
df_series_IMDB = spark.read.option("delimiter", "|").csv(path2 + 'series.csv', header=True)
df_movies_TMDB = spark.read.json(path3 + 'movies_20230524_160604.json') 
df_series_TMDB = spark.read.json(path4 + 'series_20230524_160604.json')
# Converter a coluna 'title' do DataFrame JSON para um array de palavras e extrair o ano de lançamento
df_filmes_titulos_datas = df_movies_TMDB.select(col('title'), substring(col('release_date'), 1, 4).alias('releaseDate'))

# Definir o tamanho mínimo das palavras em comum
tamanho_minimo = 4

# Realizar a filtragem dos títulos
df_movies_IMDB_trusted = df_movies_IMDB.join(df_filmes_titulos_datas,
                                   (df_movies_IMDB['tituloPincipal'].contains(df_filmes_titulos_datas['title'])) &
                                   (df_movies_IMDB['anoLancamento'] == df_filmes_titulos_datas['releaseDate']),
                                   'inner')

# Remover as colunas 'title' e 'releaseDate' do DataFrame
df_movies_IMDB_trusted = df_movies_IMDB_trusted.drop('title', 'releaseDate')

# Renomear a coluna 'tituloPincipal' para 'tituloPrincipal' no DataFrame df_IMDB_filtrado_filmes
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumnRenamed("tituloPincipal", "tituloPrincipal")

df_movies_IMDB_trusted = df_movies_IMDB_trusted.distinct()

# Trata os valores "NA" na coluna "anoFalecimento"
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))

# Converter a coluna 'name' e a substring de 'first_air_date' do DataFrame JSON para o DataFrame do TMDB
df_series_nomes_datas = df_series_TMDB.select(col('name'), substring(col('first_air_date'), 1, 4).alias('dataLancamento'))

# Realizar a filtragem dos títulos e anos de lançamento
df_series_IMDB_layer1 = df_series_IMDB.join(df_series_nomes_datas,
                                         (df_series_IMDB['tituloPincipal'].contains(df_series_nomes_datas['name'])) &
                                         (df_series_IMDB['anoLancamento'] == df_series_nomes_datas['dataLancamento']),
                                         'inner')

# Remover as colunas 'name' e 'dataLancamento' do DataFrame
df_series_IMDB_layer1 = df_series_IMDB_layer1.drop('name', 'dataLancamento')

df_series_IMDB_layer1 = df_series_IMDB_layer1.distinct()

# Renomear a coluna 'tituloPincipal' para 'tituloPrincipal' no DataFrame df_IMDB_filtrado_filmes
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Filtrar apenas os títulos das séries correspondentes aos filmes
df_filmes_correspondentes = df_movies_IMDB_trusted.select(col('tituloPrincipal').alias('titulo'))

# Realizar a junção entre os dataframes de séries e títulos correspondentes usando contains
df_series_IMDB_trusted = df_series_IMDB_layer1.join(df_filmes_correspondentes,
                                            df_series_IMDB_layer1['tituloPrincipal'].contains(df_filmes_correspondentes['titulo']),
                                            'inner')

df_series_IMDB_trusted = df_series_IMDB_trusted.drop('titulo')

# Remover linhas duplicadas no resultado
df_series_IMDB_trusted = df_series_IMDB_trusted.distinct()

# Trata os valores "NA" nas colunas
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoNascimento", when(col("anoNascimento") == "\\N", None).otherwise(col("anoNascimento")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoTermino", when(col("anoTermino") == "\\N", None).otherwise(col("anoTermino")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("tempoMinutos", when(col("tempoMinutos") == "\\N", None).otherwise(col("tempoMinutos")))

# Filtrar apenas os títulos das séries correspondentes aos filmes
df_filmes_titulos = df_movies_TMDB.select(col('title').alias('titulo'))

# Realizar a junção entre os dataframes de séries e títulos correspondentes usando contains
df_series_TMDB_trusted = df_series_TMDB.join(df_filmes_titulos,
                                            df_series_TMDB['name'].contains(df_filmes_titulos['titulo']),
                                            'inner')

df_series_TMDB_trusted = df_series_TMDB_trusted.drop('titulo','backdrop_path','poster_path')

# Remover linhas duplicadas no resultado
df_series_TMDB_trusted = df_series_TMDB_trusted.distinct()

# Trata os valores "NA" nas colunas
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("first_air_date", when(col("first_air_date") == "", None).otherwise(col("first_air_date")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("genre_ids", when(size(col("genre_ids")) == 0, None).otherwise(col("genre_ids")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("overview", when(col("overview") == "", None).otherwise(col("overview")))

# remove os colunas não relevantes
df_movies_TMDB_trusted = df_movies_TMDB.drop('adult','backdrop_path','poster_path','video')

# Obtém a data atual para criar os diretórios correspondentes
current_date = datetime.now()
ano = current_date.strftime("%Y")
mes = current_date.strftime("%m")
dia = current_date.strftime("%d")

# Define os caminhos de destino no S3 para os DataFrames no formato Parquet
path_trt_local_movies = "s3://data-lake-do-fabricio/TRT/Local/Filmes/{ano}/{mes}/{dia}/"
path_trt_local_series = "s3://data-lake-do-fabricio/TRT/Local/Series/{ano}/{mes}/{dia}/"
path_trt_tmdb_movies = "s3://data-lake-do-fabricio/TRT/TMDB/Filmes/{ano}/{mes}/{dia}/"
path_trt_tmdb_series = "s3://data-lake-do-fabricio/TRT/TMDB/Series/{ano}/{mes}/{dia}/"

# Salva os DataFrames no formato Parquet no S3
df_movies_IMDB_trusted.write.parquet(path_trt_local_movies.format(ano=ano, mes=mes, dia=dia))
df_series_IMDB_trusted.write.parquet(path_trt_local_series.format(ano=ano, mes=mes, dia=dia))
df_movies_TMDB_trusted.write.parquet(path_trt_tmdb_movies.format(ano=ano, mes=mes, dia=dia))
df_series_TMDB_trusted.write.parquet(path_trt_tmdb_series.format(ano=ano, mes=mes, dia=dia))

# Finaliza o Job
job.commit()