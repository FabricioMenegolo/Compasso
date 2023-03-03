# 1.
# Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas
# o ano em que ele completará 100 anos.
# Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem').
# Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.
from datetime import datetime
def ano_faz_cem ():
    nome = input('Digite seu nome:')
    idade = int(input('Digite sua idade:'))
    return (datetime.today().year + (100-idade))

print(ano_faz_cem())


# 2.
#Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares.
# Para cada número, imprima o Par: ou Ímpar: e o número correspondente.

for i in range(1,4):
    numero = int(input('Escreva um numero: '))
    if (numero % 2) == 0:
        print(f' Par: {numero}')
    else:
        print(f' Ímpar: {numero}')

# 3.
#Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
# Dica: Utilize a função range().

for i in range(0,21):
    if (i % 2) == 1:
        continue
    print(i)

# 4.
# Escreva um código Python que imprime todos os números primos de 1 até 100.
# Abaixo uma imagem de exemplo dos números primos entre 1 e 1000

cont = 2
for i in range(2,101):
    for j in range(2,i):
        if ((i % j) == 0):
            break
    else:
       print(i)


# 5.
# Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e 
# imprime a data completa no formato a seguir:
# Exemplo: 22/10/2022
# Importante: É necessário formatar as variáveis como strings antes de concatená-las e imprimi-las na tela.

dia, mes, ano = 22, 10, 2022
print(f'{dia}/{mes}/{ano}')


#
#6.
#Dada duas listas como as no exemplo abaixo:

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições).
O seu programa deve funcionar para listas de qualquer tamanho.
"""

def inner_join(list_a, list_b):
    lista_a = set(list_a)
    lista_b = set(list_b)
    nova_lista = []
    for i in lista_a:
        if (i in lista_b):
            nova_lista.append(i)
    
    return nova_lista

print(inner_join(a,b))

#
#7.
# Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista contendo apenas números ímpares.
def somente_pares(array):
    nova_lista=[]
    for i in range(len(array)):
        if (array[i] % 2) != 0:
            nova_lista.append(array[i])
    return nova_lista

print(somente_pares(a))


#8.
#Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
# é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

def palindromo(string, ini=0, fim=None):
    if fim is None:
        fim = len(string)-1
    if ini == fim:
        print("A palavra: " + string + " é um palíndromo")        
    elif string[ini] == string[fim]:
        return palindromo(string, ini +1, fim-1)
    else:
        print("A palavra: " + string + " não é um palíndromo")
        
list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(list)):
  palindromo(list[i])

"""
vou resumir, pois como o curso começa com funções, acabei fazendo o codigo como uma função 
na verdade eu particulamente retornaria um boleano ao invés de um print na função acima para poder
ter a possibilidade de reutilização em outros treços de codigos tornando-o mais versátil
"""

list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for string in list:
    if string == i[::-1]:
        print("A palavra: " + string + " é um palíndromo")
    else:
        print("A palavra: " + string + " não é um palíndromo")


 #
 # 9
 # Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
"""""
#Faça um programa que imprima o dados na seguinte estrutura: 
# "índice - primeiroNome sobreNome está com idade anos".

#Exemplo:
#0 - João Soares está com 19 anos 

# Você deve Utilizar a função enumerate().
"""
for i, primeirosNomes in enumerate(primeirosNomes):
    pessoa = f"{i} - {primeirosNomes} {sobreNomes[i]} está com {idades[i]} anos"
    print(pessoa)

#
#10
#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
# Utilize a lista a seguir para testar sua função.
exercicio_10 = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def distinct(lista):
    lista_distinta = []
    lista = set(lista)
    for i in lista:
        lista_distinta.append(i)
    
    return lista_distinta
    
print(distinct(exercicio_10))