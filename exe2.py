'''
    Exercicio 02

    IPE - Lsita Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

    02 – Escrever um algoritmo que produza na tela um triângulo de Pascal de
         grau “n” usando uma matriz. Abaixo temos um triângulo de Pascal de
         grau 6 (isto é, com seis linhas)
    
'''

print("Triangulo de Pascal")

linhas = int(input("Digite um numero para o triangulo pascal: "))

l = [1]
c = [0]

for i in range(linhas):
        print(l)
    
        l = [i + d for i, d in zip(l + c, c + l)]

    
