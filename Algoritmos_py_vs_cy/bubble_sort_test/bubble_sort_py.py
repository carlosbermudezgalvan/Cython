# Fecha: Noviembre - 2022
# Autor: Carlos Bermudez
# Materia: Computación paralela y distribuida
# Temas: Cython vs Python comparativa rendimiento
#------------------------------------------------------------
# Archivo python con algoritmo de ordenamiento bubble sort,
# el cual posee una complejidad de O(n elevado 2), siendo n el 
# tamaño de la entrada. 
#------------------------------------------------------------
# NOTA: bubble_sort_py y bubble_sort_cy reciben los mismos 
#       argumentos necesarios para su ejecucion
#------------------------------------------------------------
def ordenamiento_burbuja(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp

numeros =[]
for i in range(10000):
    numeros.append(100-i)
ordenamiento_burbuja(numeros)
