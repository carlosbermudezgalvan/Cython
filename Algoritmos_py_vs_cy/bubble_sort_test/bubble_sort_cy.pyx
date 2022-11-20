# Fecha: Noviembre - 2022
# Autor: Carlos Bermudez
# Materia: Computación paralela y distribuida
# Temas: Cython vs Python comparativa rendimiento
#------------------------------------------------------------
# Archivo cython con algoritmo de ordenamiento bubble sort,
# el cual posee una complejidad de O(n elevado 2), siendo n el 
# tamaño de la entrada. 
#------------------------------------------------------------
# NOTA: bubble_sort_py y bubble_sort_cy reciben los mismos 
#       argumentos necesarios para su ejecucion
#------------------------------------------------------------
cython: language_level=3
def ordenamiento_burbuja(list lista):
    cdef int n, i, temp
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp