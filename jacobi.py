#Importar librerias
import numpy as np
import os

""" #Para Windows
os.system('cls') """

#Para Linux y MacOS
os.system('clear')

#Función principal
def main():
    print("- - Método de Jacobi - -")

    #Obtención de datos
    print("\nIngrese los coeficientes de cada ecuación separados por un espacio: ")
    coeficientes = list(map(float, input().split()))  
    A = np.array(coeficientes).reshape(3, 3)

    print("\nIngrese los resultados de cada ecuación separados por un espacio: ")
    resultados = list(map(float, input().split()))  
    B = np.array(resultados).reshape(3, 1)

    Es = float(input("\nIngrese la tolerancia del sistema (Es) en porcentaje: \n"))

    #Llamada a función del método 
    jacobi(A,B,Es)

#Función para el método
# x^i = D^-1 (L+U)x^i-1 + D^-1
def jacobi(A,B,Es):
    contador = 1
    x = [[0], [0], [0]]
    Ea = [100, 100, 100]

    #Repetir hasta que el error absoluto sea menor a la tolerancia
    while Ea[0] > Es and Ea[1] > Es and Ea[2] > Es:
        Ea = np.array(Ea, dtype = np.float32)
        diagonal = np.diag(np.diag(A))
        LU = A - diagonal
        diagonalInv = np.linalg.inv(diagonal)
        xi = [x[0], x[1], x[2]]
        x = np.dot(diagonalInv, np.dot(-LU, x)) + np.dot(diagonalInv, B)

        #Obtención del error absoluto
        for i in range(3):
            Ea[i] = np.linalg.norm((x[i] - xi[i]) / x[i]) * 100

        #Impresión de resultados
        print("\nIteración #", contador)
        print("\nLa matriz X es:\n", x)
        print("\nEl error absoluto es: ", Ea, "\n")

        contador += 1

#Llamada a función principal
main()

""" Ejemplo 1
3 -0.1 -0.2 0.1 7 -0.3 0.3 -0.2 10
7.85 -19.3 71.4
1 """

""" Ejemplo 2
10 2 -1 -3 -6 2 1 1 5
27 -61.5 -21.5
5 """