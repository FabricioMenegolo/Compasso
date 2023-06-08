-- Criação da view movies_dim
CREATE OR REPLACE VIEW movies_dim AS
SELECT
  id AS movie_id,
  genre_ids,
  title,
  tempoMinutos,
  release_date,
  original_language,
  popularity,
  CAST(nota_media AS DOUBLE) AS nota_media,
  votos
FROM Dash.movies_tb;

-- Criação da view series_dim
CREATE OR REPLACE VIEW series_dim AS
SELECT
  id AS series_id,
  genre_ids,
  name,
  tempoMinutos,
  first_air_date,
  anoTermino,
  original_language,
  popularity,
  CAST(nota_media AS DOUBLE) AS nota_media,
  votos
FROM dash.series_tb;

-- Criação da view actors_dim
CREATE OR REPLACE VIEW actors_dim AS
SELECT
  id AS actor_id,
  personagem,
  nomeArtista,
  generoArtista,
  CAST(anoNascimento AS INT) AS anoNascimento,
  CAST(anoFalecimento AS INT) AS anoFalecimento,
  profissao,
  titulosMaisConhecidos
FROM dash.actors_tb;

-- Criação da view fato_actors_movies
CREATE OR REPLACE VIEW movies_series_combined_dim AS
SELECT
  id,
  genre_ids,
  title,
  CAST(tempoMinutos AS int) AS tempoMinutos,
  release_date AS dataLancamento,
  original_language,
  popularity,
  nota_media,
  votos,
  'Filme' AS tipo
FROM
  Dash.movies_tb
UNION ALL
SELECT
  id,
  genre_ids,
  name AS title,
  tempoMinutos,
  first_air_date AS dataLancamento,
  original_language,
  popularity,
  nota_media,
  votos,
  'Série' AS tipo
FROM
  dash.series_tb;
