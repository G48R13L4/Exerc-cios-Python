'''
    Exercício 03

    IPE - Lista Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   3-Escreva uma classe que leia um vetor de 30 posições de números inteiros e imprimir, logo após, gerar
   2 vetores a partir dele, um contendo os elementos de posições ímpares do vetor e o outro os elementos
   pares. Imprimi-los no final.

'''
núm = [[], []]
i = 0

for c in range(1, 30):
  i = int(input(f'Digite o{c}° valor:'))
  if i%2 ==0:
    núm[1].append(i)
  else:
    núm[0].append(i)

print('-='*40)
núm[0].sort()
núm[1].sort()
print(f'Todos os valores ímpares :{núm[0]}')
print(f'Todos os valores pares:{núm[1]}')

