-- View Vendas por Combustível
CREATE VIEW vw_vendas_combustivel AS
SELECT tb_combustivel.tipoCombustivel, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes
FROM tb_locacao
JOIN tb_carro ON tb_locacao.idCarro = tb_carro.idCarro
JOIN tb_combustivel ON tb_carro.idcombustivel = tb_combustivel.idcombustivel
GROUP BY tb_combustivel.tipoCombustivel
ORDER BY valor_total_locacoes DESC;

-- View Desempenho do Vendedor
CREATE VIEW vw_desempenho_vendedor AS
SELECT tb_vendedor.nomeVendedor, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_vendedor ON tb_locacao.idVendedor = tb_vendedor.idVendedor
GROUP BY tb_vendedor.nomeVendedor
ORDER BY media_valor_locacoes DESC;

-- View Locações por Modelo de Carro
CREATE VIEW vw_locacoes_modelo_carro AS
SELECT tb_carro.modeloCarro, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_carro ON tb_locacao.idCarro = tb_carro.idCarro
GROUP BY tb_carro.modeloCarro
ORDER BY quantidade_locacoes DESC;

-- View Locações por Cliente
CREATE VIEW vw_locacoes_cliente AS
SELECT tb_cliente.nomeCliente, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_cliente ON tb_locacao.idCliente = tb_cliente.idCliente
GROUP BY tb_cliente.nomeCliente
ORDER BY media_valor_locacoes DESC;

-- View Locações por Período Acumulado por Mês (independentemente do ano)
CREATE VIEW vw_locacoes_periodo AS
SELECT substr(tb_locacao.dataLocacao, 5, 2) AS periodo_mes,
       COUNT(*) AS quantidade_locacoes,
       SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes,
       AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
GROUP BY substr(tb_locacao.dataLocacao, 5, 2);
