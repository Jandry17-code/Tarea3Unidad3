#JANDRY STEVEN GARCES ROSALES
#TAREA3UNIDAD3
#Modificar el archivo de series.py y poner una función. Indicar los comentarios sus nombres y apellidos.



def sumar_numeros(lista):
    """
    Suma todos los números en una lista.

    Parámetros:
    lista (list): Lista de números a sumar.

    Retorna:
    int: La suma total de los números en la lista.
    """
    return sum(lista)


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5] 
    print(sumar_numeros(numeros))