"""
Armazene o arquivo actors.csv dentro de uma nova pasta, após isso crie 5 arquivos do tipo “txt” vazios 
(1 para cada exercício do desafio).

Em seguida para cada uma das tarefas da sequencia, leia o arquivo actors.csv utilizando Python
como linguagem de programação e depois de obter as repostas necessárias armazene cada um dos resultados
em um dos arquivos “txt” criados.

Pontos de Atenção:

Para desenvolvimento deste exercício, não deve ser utilizado as bibliotecas Pandas e NumPy e/ou 
outras bibliotecas e engines que utilizam de dataframes.

Todas as transformações que julgarem necessárias, devem ser feitas utilizando os scripts
Python e nenhuma modificação deve ser feita no arquivo actors.csv

Para leitura do arquivo actors.csv, não deve ser utilizado o módulo csv nativo do Python.

Perguntas dessa tarefa
1. O ator/atriz com maior número de filmes e o respectivo número de filmes.

2. A média do número de filmes por autor.

3. O ator/atriz com a maior média por filme.

4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

5. A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
"""
#pergunta1
"""
from csv import DictReader
path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = i["Number of Movies"]
        resultado.append([ator, num_filmes])
print(resultado)

resultado.sort(key=lambda x: x[1], reverse=True)
print(resultado[0])

with open( path +'Pergunta_1.txt', 'w') as resposta1:
    resultado1=resultado[0]
    resposta1.write(str(resultado1))
"""
#    ___________

from csv import DictReader
path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    num_filmes_total = 0

    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = int(i["Number of Movies"])
        resultado.append([ator, num_filmes])
        num_filmes_total += num_filmes

resultado2 = num_filmes_total/len(ator)

with open( path +'Pergunta_2.txt', 'w') as resposta2:
    resultado2=resultado[0]
    resposta2.write(str(resultado2))


