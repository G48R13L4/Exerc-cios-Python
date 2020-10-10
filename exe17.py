'''
    Exercício 17

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   17- Desenvolver um programa que calcule a média aritmética simples das notas de um aluno com opção
    de escolha para entrada de 2 notas, 3 notas ou 4 notas. Exiba no final o nome do aluno e sua média com a
    informação: “Aprovado” se média maior ou igual a 7, “Reprovado” se média menor que 4 e “Exame” nos
    demais casos. (utilizar laço de repetição com opção de saída do sistema).

'''


name = input('Nome do Aluno: ')
notas = int (input("Entre com a quantidade de notas: "))
if (notas == 2 ):
    np1 = float(input("Entre com a nota NP1: "))
    np2 = float(input("Entre com a nota NP2: "))

    ms = (np1 + np2)/2

    if (ms >= 7):
        status = 'Aprovado sem exame'

    if (ms < 4):
        status = 'Reprovado com exame'

elif (notas == 3 ):
    np1 = float(input("Entre com a nota NP1: "))
    np2 = float(input("Entre com a nota NP2: "))
    np3 = float(input("Entre com a nota NP3: "))

    ms = (np1 + np2+ np3) / 3

    if (ms >= 7):
        status = 'Aprovado sem exame'

    if (ms < 4):
        status = 'Reprovado com exame'

elif (notas == 4 ):
    np1 = float(input("Entre com a nota NP1: "))
    np2 = float(input("Entre com a nota NP2: "))
    np3 = float(input("Entre com a nota NP3: "))
    np4 = float(input("Entre com a nota NP4: "))

    ms = (np1 + np2 + np3 + np4) / 4

    if (ms >= 7):
        status='Aprovado sem exame'

    if (ms < 4):
        status='Reprovado com exame'

else:
    print('Valor de notas inválido')


print(f'O aluno(a): {name}')
print(f'tem a média: {ms}')
print(f'situação:{status}')