'''
    Exercício 03

    IPE - Lista Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   5-Preencher por leitura uma matriz M (5,5). Em seguida, calcular e imprimir a matriz toda e a média dos
   elementos das áreas assinaladas abaixo:

'''

matriz = [[],[],[],[],[]]
soma = med1 = med2 = med3 = med4 = med5 = med6 = media =0

for l in range(0,5):
        for c in range(0,5):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,5):
        for c in range(0,5):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print('-='*30)
for s in range(0,5):
        soma += matriz [l][c]

for m in range(0,5):
        med1 += matriz [2][1]
        med2 += matriz [3][1]
        med3 += matriz [3][2]
        med4 += matriz[4][1]
        med5 += matriz [4][2]
        med6 += matriz[4][3]

for med in range(0,5):
        media = (med1 + med2 + med3 + med4 + med5 + med6) / 5

print(f'O cálculo da matriz toda é: {soma}')
print(f'a média: {media}')
