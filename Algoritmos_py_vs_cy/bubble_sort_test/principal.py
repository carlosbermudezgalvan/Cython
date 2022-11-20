import time
import random
import bubble_sort_cy
import bubble_sort_py

formato_datos = "{:.5f}, {:.5f}\n"

entradas = 10000
muestras_test = 40

numeros = []
for i in range(entradas):
    numeros.append(random.randint(0,entradas+100))
    
for i in range(muestras_test):
    
        ini_time = time.time()
        bubble_sort_py.ordenamiento_burbuja(numeros)
        fin_time = time.time()
        final_time = fin_time - ini_time

        ini_time2 = time.time()
        bubble_sort_cy.ordenamiento_burbuja(numeros)
        fin_time2 = time.time()
        final_time2 = fin_time2 - ini_time2

        with open("bubble_results.csv","a") as archivo:
            archivo.write(formato_datos.format(final_time, final_time2))