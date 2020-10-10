'''
    Exercício 11

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   11- Construa um programa que, para um grupo de 50 valores inteiros, determine:
    a) A soma dos números positivos;
    b) A quantidade de valores negativos;

'''

núm = []
soma = negativos = 0


for c in range(1, 50):
    i = int(input(f'Digite o {c}° valor:'))
    if i>=1:
        soma = soma + i
    else:
        negativos = negativos + 1




print(f'Soma dos números positivos: {soma}')
print(f'Quantidade de valores negativos:{negativos}')




