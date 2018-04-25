#!/usr/bin/env python3
def funcao3():
    horaAtual=int(input())
    despertador=int(input())
    hora = despertador%24
    if horaAtual+hora > 24:
        horaAtual+=hora-24
    else:
        horaAtual+=hora
    print("O despertador tocara as: "+str(horaAtual))

funcao3()
        
