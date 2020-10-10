'''
    Exercício 13

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   13-Desenvolva um programa que receba nome, idade e salário digitados pelo usuário e apresente no final
    quantas dessas idades estão entre 15 e 17 anos, quantas são maiores de 21 anos, quantos salários estão
    entre R$1.500,00 e R$2.000,00, quantos estão acima de R$3.500,00 e qual é o maior e o menor salário
    digitado. (utilizar laço de repetição com opção de saída do sistema).

'''

menoridade = maioridade= 0

sall1 = sall2 = 0

maiorsall = menorsall = 0


for c in range(1, 5):
  nome = input(f'Digite o {c}° Nome: ')
  idade = int(input(f'Digite a {c}° Idade: '))
  salario = float(input(f'Digite o {c}° Salário: '))


print('-='*30)
if (idade >= 15 and idade <= 17):
     menoridade = menoridade + 1
elif(idade>21):
  maioridade = maioridade + 1


if salario == 0:
     maiorsall = salario
elif salario>maiorsall:
  maiorsall = salario

if salario == 0:
     menorsall = salario
elif salario<menorsall:
  menorsall = salario



print(f'Quantidade de salários entre R$1.500,00 e R$2.000,00: {sall1}')
print(f'Quantidade de salários acima de R$3.500,00: {sall2}')
print('-='*30)
print(f'Quantidade de idades entre 15 e 17 anos: {menoridade}')
print(f'Quantidade de idades maiores que 21 anos:{maioridade}')
print('-='*30)
print(f'O maior salário: {maiorsall}')
print(f'O menor salário:{menorsall}')