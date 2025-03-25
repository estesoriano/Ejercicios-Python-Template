# coding=utf-8
__Author__="Estefania Soriano"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# Implemente función obtenerCalificacion
def obtenerCalificaion(nota) :
    if 0 <= nota < 3:
        calificacion = "Muy deficiente"
    elif 3 <= nota < 5:
        calificacion = "Insuficiente"
    elif 5 <= nota < 6:
        calificacion = "Suficiente"
    elif 6 <= nota < 7:
        calificacion = "Bien"
    elif 7 <= nota < 9:
        calificacion = "Notable"
    elif 9 <= nota <= 10:
        calificacion = "Sobresaliente"
    else:
        calificacion = "Incorrecta"
    return calificacion
   # Implemente aquí ... Si (condición) entonces ... sino ... si (condición) entonces ... sino ...


# Programa principal
def main():
    n=int(input("Introduzca la nota: "))
    print('Calificación: '+obtenerCalificaion(n))

if __name__== "__main__" :
   main()
