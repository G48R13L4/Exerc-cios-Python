'''
    Exercicio 02

    IPE - Lsita Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

    12 - Desenvolva um programa que receba 25 números (tipo float) digitados pelo usuário e apresente no final a quantidade de números positivos, negativos, zeros, pares e ímpares digitados. 
    
'''

x = 1
p = 0
n = 0
z = 0
pa = 0
im = 0

while x <= 25:
    numero = float(input(f"Entre com {x}° numero: "))

    x = x + 1

    if(numero == 0):
        z += 1

    else:
        if(numero > 0):
            p += 1

        if(numero < 0):
            n += 1

        if(numero % 2 == 0):
            pa += 1

        if(numero % 2 != 0):
            im = im + 1

print("A qtd de números pares é: ", pa)
print("A qtd de números ímpares é: ", im)
print("A qtd de números positovs é: ", p)
print("A qtd de números negativos é: ", n)
