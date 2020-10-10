'''
    Exercício 15

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   15- Elabore um programa que receba dois números (tipo float) digitados pelo usuário e pergunte qual
    operação ele deseja realizar. Operações possíveis: soma, subtração, multiplicação, divisão, maior e menor
    número. Exiba no final os números digitados e o resultado da operação escolhida.

'''
import char as char

operacao = input('Qual operação deseja realizar? ')
if operacao == '+' :
    valor1 = float(input("Entre com o Primeiro valor: "))
    valor2 = float(input("Entre com o Segundo valor: "))

    result = (valor1 + valor2)


elif operacao == '-' :
    valor1 = float(input("Entre com o Primeiro valor: "))
    valor2 = float(input("Entre com o Segundo valor: "))

    result = (valor1 - valor2)

elif operacao == '*' :
    valor1 = float(input("Entre com o Primeiro valor: "))
    valor2 = float(input("Entre com o Segundo valor: "))

    result = (valor1 * valor2)

elif operacao == '/':
    valor1 = float(input("Entre com o Primeiro valor: "))
    valor2 = float(input("Entre com o Segundo valor: "))

    result = (valor1 / valor2)


else:
    print('Operação inválida')

print(f'O resultado é: {result}')