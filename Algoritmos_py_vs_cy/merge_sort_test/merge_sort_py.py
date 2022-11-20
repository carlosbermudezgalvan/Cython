# Fecha: Noviembre - 2022
# Autor: Carlos Bermudez
# Materia: Computación paralela y distribuida
# Temas: Cython vs Python comparativa rendimiento
#------------------------------------------------------------
# Archivo python con algoritmo de ordenamiento merge sort,
# el cual posee una complejidad de O(n log n), siendo n el 
# tamaño de la entrada 
#------------------------------------------------------------
# NOTA: orbita_cy y orbite_py reciben los mismos argumentos
#       necesarios para su ejecucion
#------------------------------------------------------------
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1
        
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1
        
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1

numeros =[]
for i in range(1000000):
    numeros.append(100-i)
merge_sort(numeros)