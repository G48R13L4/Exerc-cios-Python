'''
    Exercicio 02

    IPE - Lsita Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

    14 – Desenvolva um programa que receba nome e salário de um funcionário e calcule o valor do salário líquido desse funcionário, utilizando função, descontando os impostos INSS e Imposto de Renda (IR) conforme tabela oficial vigente. (utilizar laço de repetição com opção de saída do sistema).  
    
'''

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario do funcionario para o calculo dos descontos: "))
ir = salario * 0.075
inss = salario * 0.075

sall = round(salario - (ir + inss), 2)



print("Funcionario: ",nome,"tem um salário liquido de: R$%4.2f" , sall )
