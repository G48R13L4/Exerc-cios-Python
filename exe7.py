'''
    Exercício 07

    IPE - Lista Exercícios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

   07-Escrever um algoritmo que lê um par de coordenadas (x,y) inteiras e imprima uma mensagem
    informando em qual quadrante está o ponto. O algoritmo deve também ser capaz de identificar se o ponto
    está sobre um dos eixos ou no ponto central

'''
x= int(input('Digite a Coordenada X: '))
y= int(input('Digite a Coordenada Y: '))


if x ==0 and y ==0:
    quadrante = 0
    print(f'O quadrante é igual a 0')

elif x ==0 or y==0:
    quadrante= -1

elif x>0:
    if y>0:
      quadrante = 1
    elif y>0:
        quadrante = 4
elif y>0:
    if y > 0:
        quadrante = 2
    elif y > 0:
        quadrante = 3

print('O ponto (%d, %d) pertence ao quadrante %d' %(x,y,quadrante))