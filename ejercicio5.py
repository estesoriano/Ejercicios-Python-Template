# coding=utf-8
__Author__="Estefania Soriano"

import random

# Función que determina si un numero es par.

def esPar(numero) :
    if(numero % 2 == 0):
        return True
    else:
        return False # --> Implemente código de la función <--

def esImpar(numero) :
    if(numero % 2 != 0):
        return True
    else:
        return False # --> Implemente código de la función <--

def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    if esImpar(inicio) :
        numero=inicio+1
    
    contador = 0
    while contador < valores:
        if esPar(numero):
            pares.append(numero)
            contador=contador+1
        numero=numero+1
    
    return pares

def generarImpares(valores, inicio) :
    impares=[]
    numero=inicio
    if esPar(inicio) :
        numero=inicio+1

    contador = 0
    while contador < valores:
        if esImpar(numero):
            impares.append(numero)
            contador=contador+1
        numero=numero+1

    return impares


# Programa principal
def main():
    print("Par e impar")
    n=int(input("Introduzca un numero: "))
    print("{0} es par --> {1}.".format(n,esPar(n)))
    m=int(input("Introduzca el número de valores: "))
    i=int(input("Introduzca el número inicial: "))
    x=generarPares(m,i)
    y=generarImpares(m,i)
    print("Impares: ",y)
    print("Pares: ",x)    

if __name__== "__main__" :
   main()
