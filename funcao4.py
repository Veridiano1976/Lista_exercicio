#!/usr/bin/env python3
def funcao4():
    semana = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
    mes = int(input("Digite o dia do mes que voce viajará\n"))
    diaSemana = input("Digite o dia da semana que voce viajará\n")
    duracao = int(input("Digite quantos dias a viagem vai durar\n"))
    dias = duracao%7
    indiceDia = semana.index(diaSemana)
    if dias + indiceDia > 7:
        indiceDia+=dias -7
    else:
        indiceDia+=dias
        
    print("O dia em que voce voltara eh: " + semana[indiceDia])
    
funcao4()




        
