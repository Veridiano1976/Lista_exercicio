#!/usr/bin/env python3

def funcao7():
    p = 10000
    n = 12
    r = 0.08
    t = int(input("Digite o numero de anos\n"))
    a = p * (((1 + (r/n)) ** (n*t)))
    print("{:.2f}".format(a))
    
funcao7()


