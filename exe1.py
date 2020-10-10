'''
    Exercício 01

    IPE - Lista Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

    1- Desenvolva uma classe que apresente todos os números primos existentes entre N1 e N2, em que N1
    e N2 são números naturais fornecidos. Um número é primo quando é divisível somente por ele e pela unidade
    (1).

'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
c = 0

for i in range(1, num1+1):
    if num1 % i == 0:
        print(f'\033[0;33m{i}\033[m', end=' ')
        c += 1
    else:
        print(f'\033[0;31m{i}\033[m', end=' ')
if num1 % 2 == 0:
    print(f'\nO número {num1} foi divisível {c} vezes')
    print('Então ele não é um numero primo.')
else:
    print(f'\nO número {num1} foi divisível apenas {c} vezes')
    print(f'Então ele é um numero primo.')

