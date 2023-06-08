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

-- Criação da tabela fato_actors_movies
CREATE OR REPLACE VIEW fato_actors_movies AS
SELECT
  ROW_NUMBER() OVER (ORDER BY a.id, m.id) AS id,
  a.id AS actor_id,
  m.movie_id
FROM dash.actors_tb a
JOIN Dash.movies_tb m ON a.id = m.movie_id;

-- Criação da tabela fato_actors_series
CREATE OR REPLACE VIEW fato_actors_series AS
SELECT
  ROW_NUMBER() OVER (ORDER BY a.id, s.id) AS id,
  a.id AS actor_id,
  s.seriesId AS series_id
FROM dash.actors_tb a
JOIN dash.series_tb s ON a.id = s.seriesId;
