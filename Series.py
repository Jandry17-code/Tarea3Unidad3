# JANDRY STEVEN GARCES ROSALES
# Archivo: series.py

def generar_serie_pares(n):
    """
    Genera una serie de los primeros 'n' números pares.

    Parámetros:
    n (int): Cantidad de números pares a generar.

    Retorna:
    list: Lista con los primeros 'n' números pares.
    """
    if n <= 0:
        return []

    return [2 * i for i in range(n)]

if __name__ == "__main__":
    num_terminos = 10  # Puedes cambiar el número de términos deseado
    print(generar_serie_pares(num_terminos))


# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l