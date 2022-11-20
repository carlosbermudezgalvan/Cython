import time
import random
import merge_sort_cy
import merge_sort_py

formato_datos = "{:.5f}, {:.5f}\n"

entradas = 2000000
muestras_test = 40

numeros = []
for i in range(entradas):
    numeros.append(random.randint(0,entradas+100))
    
for i in range(muestras_test):
    
        ini_time = time.time()
        merge_sort_py.merge_sort(numeros)
        fin_time = time.time()
        final_time = fin_time - ini_time

        ini_time2 = time.time()
        merge_sort_cy.merge_sort(numeros)
        fin_time2 = time.time()
        final_time2 = fin_time2 - ini_time2

        with open("merge_sort_results.csv","a") as archivo:
            archivo.write(formato_datos.format(final_time, final_time2))