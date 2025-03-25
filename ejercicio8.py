# coding=utf-8
__Author__="Estefania Soriano"


# Función que determina si un numero es primo.

def fibonacci(n) :
    vector = []

    if n<1 :
        return vector
    elif n==1 :
        vector.append(1)
        return vector
    elif n >=2 :
        # Implementa las series de Fibonacci
        # vector[0]=1
        # vector[1]=1

        vector.append(1)
        vector.append(1)
        # Creamos aquí el bucle WHILE
        contador=2

        while contador < n:
            siguientenumero=vector[contador - 1] + vector[contador - 2]
            vector.append(siguientenumero)
            contador=contador+1

    return vector; # Retorno de la función

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero=int(input("Introduzca un numero: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero,fibonacci(numero)))

if __name__== "__main__" :
   main()
