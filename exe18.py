'''
    Exercicio 02

    IPE - Lsita Exercicios 2020-2
    Nomes: Fernando Martins/ Gabriela Ferreira
    RMs: N6742B8 /N603FC7

    Professor: Vinicius Heltai
    Data: Outubro/2020
    2° Semestre-UNIP

     Desenvolver um programa que entre com as notas (NP1 e NP2), quantidade de falta e carga horaria da disciplina e informe se o aluno “Passou Direto”, “Exame”, “Substitutiva” ou “Reprovado”. Caso o aluno entre com “NC” o aluno deve realizar a PSUB. Caso o aluno fique com nota insatisfatória, deve realizar um exame e após o lançamento, o programa deve reanalisar a situação, acrescentando “Aprovado após exame” ou 
     PÁGINA 5 DE 6 
     “Reprovado após exame”. A regra deve ser a mesma do Manual do Aluno '''


print("<<<<<<<<Programa de nota para avaliar a situação do aluno(a)>>>>>>>>>\n")

np1 = int(input("Digite a 1° nota do aluno(a): "))
np2 = int(input("Digite a 2° nota do aluno(a): "))
falta = int(input("Digite a quantidade de faltas do aluno(a): "))
cargaHoraria = int(input("Digite a quantidade de carga horaria: "))
porcent = 100 - (falta/cargaHoraria) * 100

if (porcent < 75):
    print("Reprovado(a) por falta")
    print(f"Presença: {porcent} %")

else:

    
    m = (np1 + np2) / 2

    if(m >= 6.7 and m < 7):
        m = 7
        
    if(m >= 7):
        mf = m
        ex = "NA"
        st = "Aprovado sem exame"

    else:
        ex = float(input("Digite a nota do EXAME: "))
        mf = (m + ex) / 2

    if(mf >= 4.75 and mf < 5):
        mf = 5
        
    if(mf >= 5):
        st = "Aprovado com exame"
        
    else:
        st = "Reprovado apos o exame"

    print(f"NP1: {np1:.1f} ### NP2: {np2:.1f} ")
    print (f"M: {m:.1f}   ### EXAME: {ex}  ### MF: {mf:.1f}")
    print(f"FALTAS: {falta} ### {porcent:.2f} % de presença")
    print(f"ST: {st}")
    

