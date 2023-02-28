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
        print(f' {numero} é par')
    else:
        print(f' {numero} é impar')

# 3.
#Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
# Dica: Utilize a função range().

for i in range(1,21):
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