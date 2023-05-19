/*
Escolhi esse conjunto de tabelas a fim de abranger diferentes aspectos das
 locações de carros, como tipo de combustível, o desempenho individual dos 
 vendedores, as locações por modelo de carro e por cliente, e o acompanhamento 
 do desempenho das locações ao longo do tempo, por período acumulado mensalmente. 
Isso permite a análise dos dados a partir de diversas perspectivas, facilitando a
 compreensão do desempenho do negócio e a identificação de padrões e tendências 
 podendo gerar alguns insights para tomada de decisões estratégicas.
*/

-- View Vendas por Combustível
-- Isso pode ajudar a tomar decisões estratégicas relacionadas à oferta de veículos com base na demanda por tipos específicos de combustível.
CREATE VIEW vw_vendas_combustivel AS
SELECT tb_combustivel.tipoCombustivel, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes
FROM tb_locacao
JOIN tb_carro ON tb_locacao.idCarro = tb_carro.idCarro
JOIN tb_combustivel ON tb_carro.idcombustivel = tb_combustivel.idcombustivel
GROUP BY tb_combustivel.tipoCombustivel;

-- View Desempenho do Vendedor
-- Isso pode permitir a identificação dos vendedores mais produtivos e eficazes, bem como auxiliar no desenvolvimento de estratégias de incentivo e treinamento.
CREATE VIEW vw_desempenho_vendedor AS
SELECT tb_vendedor.nomeVendedor, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_vendedor ON tb_locacao.idVendedor = tb_vendedor.idVendedor
GROUP BY tb_vendedor.nomeVendedor;

-- View Locações por Modelo de Carro
--  Isso pode auxiliar na identificação de modelos populares e rentáveis, bem como na identificação de oportunidades de melhorias ou descontinuação de modelos menos procurados.
CREATE VIEW vw_locacoes_modelo_carro AS
SELECT tb_carro.modeloCarro, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_carro ON tb_locacao.idCarro = tb_carro.idCarro
GROUP BY tb_carro.modeloCarro;

-- View Locações por Cliente
-- Isso pode ajudar na segmentação de clientes e na elaboração de estratégias de fidelização e retenção, além de identificar oportunidades de upselling ou cross-selling para clientes de alto valor.
CREATE VIEW vw_locacoes_cliente AS
SELECT tb_cliente.nomeCliente, COUNT(*) AS quantidade_locacoes, SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes, AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
JOIN tb_cliente ON tb_locacao.idCliente = tb_cliente.idCliente
GROUP BY tb_cliente.nomeCliente;

-- View Locações por Período Acumulado por Mês (independentemente do ano)
-- Isso pode ajudar na elaboração de estratégias de precificação, alocação de recursos e promoções para maximizar o desempenho das locações.
CREATE VIEW vw_locacoes_periodo AS
SELECT substr(tb_locacao.dataLocacao, 5, 2) AS periodo_mes,
       COUNT(*) AS quantidade_locacoes,
       SUM(tb_locacao.vlrDiaria) AS valor_total_locacoes,
       AVG(tb_locacao.vlrDiaria) AS media_valor_locacoes
FROM tb_locacao
GROUP BY substr(tb_locacao.dataLocacao, 5, 2);
