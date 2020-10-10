'''
    Exercicio 02

    IPE - Lsita Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

     Elabore um programa que faça a conversão de moedas. O programa deve receber uma quantidade em determinada moeda e a taxa de conversão e apresentar a quantidade convertida na moeda selecionada. Conversões possíveis: dólar para real, euro para real, real para dólar e real para euro. (utilizar laço de repetição com opção de saída do sistema). 
    
'''

print("Selecione a moeda para converção: ")

m = input("Dólar para Real >>>>>> '1'\n"
          "Euro para Real >>>>>>> '2'\n"
          "Real para Dólar >>>>>> '3'\n"
          "Real para Euro >>>>>>> '4'\n")

if m == '1':
    print("<<<<<<<<<< Dólar para Real: >>>>>>>>>>")

    d = 5.54
    c = input("Digite o valor do Dólar para ser convertido para Real: ")

    resul = float(d) * float(c)

    print(" O valor em Real é: ","R$",resul,"\n")

elif m == '2':
    
     print("<<<<<<<<<< Euro para Real: >>>>>>>>>>")

     e = 6.55
     c = input("Digite o valor do Euro paraa ser convertido para Real: ")

     result = float(e) * float(c)

     print(" O valor em Real é: ","R$",result,"\n")

elif m == '3':

     print("<<<<<<<<<< Real para Dólar: >>>>>>>>>>")

     r = input("Digite o valor em Real para converção: ")
     d = 5.54

     result = float(r) / float(d)

     print("O valor em Dólar é: ",result,"\n")

elif m == '4':

    print("<<<<<<<<<< Real para Dólar: >>>>>>>>>>")

    r = input("Digite o valor em Real para converção: ")
    e = 6.55

    result = float(r) / float(e)

    print("O valor em Dólar é: ",result,"\n")

















     
     
