#Importar librerias
import numpy as np
import os

""" #Para Windows
os.system('cls') """

#Para Linux y MacOs
os.system('clear')

#Función principal
def main():
    print("- - Método de Gauss-Seidel - -")

    #Obtención de datos
    print("\nIngrese los coeficientes de cada ecuación separados por un espacio: ")
    coeficientes = list(map(float, input().split()))  
    A = np.array(coeficientes).reshape(3, 3)

    print("\nIngrese los resultados de cada ecuación separados por un espacio: ")
    resultados = list(map(float, input().split()))  
    B = np.array(resultados).reshape(3, 1)

    Es = float(input("\nIngrese la tolerancia del sistema (Es) en porcentaje: \n"))

    #Llamada a función del método 
    gaussSeidel(A,B,Es)

#Función para el método
def gaussSeidel(A,B,Es):
    contador = 1
    sizeA = len(A[0:])
    x = np.zeros((sizeA))
    Ea = [100, 100, 100]

    #Repetir hasta que el error absoluto sea menor a la tolerancia
    while Ea[0] > Es and Ea[1] > Es and Ea[2] > Es:
        xi = [x[0], x[1], x[2]]
        Ea = np.array(Ea, dtype = np.float32)

        #Obtenciónn del pivote de la matriz
        for i in range(sizeA):
            pivote = A[i,i]

            for j in range(sizeA):
                A[i,j] = A[i,j] / pivote

            B[i] = B[i] / pivote

        #Obtención de los valores de x
        for i in range(sizeA):
            sum = B[i]

            for j in range(sizeA):
                if (i != j):
                    sum = sum - A[i,j] * x[j]
        
            x[i] = sum

        #Obtención del error absoluto
        for i in range(3):
            Ea[i] = abs((x[i] - xi[i]) / x[i]) * 100

        #Impresión de resultados
        print("\nIteración #", contador)
        print("\nLa matriz X es: ", x)
        print("\nEl error absoluto es: ", Ea, "\n")

        contador += 1

#Llamada a función principal
main()

""" Ejemplo 1
3 -0.1 -0.2 0.1 7 -0.3 0.3 -0.2 10
7.85 -19.3 71.4
1 """

""" Ejemplo 2
-8 1 -2 2 -6 -1 -3 -1 7
-20 -38 -34
5 """