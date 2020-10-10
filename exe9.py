'''
    Exercício 09

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   9-Faça uma função que recebe um valor inteiro e verifica se o valor é positivo, negativo ou zero. A função
    deve retornar 1 para valores positivos, ‐1 para negativos e 0 para o valor 0.

'''

numero = int(input('Digite o valor do número: '))

print('-='*30)
if (numero >= 1):
    print(' O número é Positivo, ou seja: 1')
elif (numero <= -1):
    print('O número é Negativo, ou seja: -1')
else:
    print('O número é Equivalente a 0, ou seja:0')
