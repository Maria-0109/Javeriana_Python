#!/usr/bin/python3

def sumar(sumando1,sumando2):
    print("Resultado de la suma:\n",sumando1 + sumando2)
def restar(minuendo,sustraendo):
    print("Resultado de la resta: \n",minuendo - sustraendo)  
def multiplicar(coeficiente1,coeficiente2):
    print("Resultado de la multiplicación: \n",coeficiente1 * coeficiente2)
def potenciar(base,exponente):
    if (base==0 and exponente < 0):
        print("Error \n")
    else:
        print("Resultado de la potencia: \n",base ** exponente)

sumar(3,8)
restar(5,11)
multiplicar(4,8)
potenciar(5,2)