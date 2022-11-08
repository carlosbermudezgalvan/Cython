# Fecha: Noviembre - 2022
# Autor: Carlos Bermudez
# Materia: Computación paralela y distribuida
# Temas: Cython vs Python comparativa rendimiento

import orbita_cy
import orbita_py
import time

formato_datos = "{:.5f}, {:.5f}\n"

#Python
tierra = orbita_py.Planet()
tierra.x = 100*10**3
tierra.y = 300*10**3
tierra.z = 700*10**3
tierra.vx = 2.00*10**3
tierra.vy = 29.87*10**3
tierra.vz = 0.034*10**3
tierra.m = 5.97424*10**3

#Cython
tierraCy = orbita_cy.Planet()
tierraCy.x = 100*10**3
tierraCy.y = 300*10**3
tierraCy.z = 700*10**3
tierraCy.vx = 2.00*10**3
tierraCy.vy = 29.87*10**3
tierraCy.vz = 0.034*10**3
tierraCy.m = 5.97424*10**3

time_span = 400
n_steps = 2000000

formateo_datos = ""

for i in range(10):

        ini_time = time.time()
        orbita_py.step_time(tierra, time_span, n_steps)
        fin_time = time.time()
        final_time = fin_time - ini_time

        ini_time2 = time.time()
        orbita_cy.step_time(tierraCy, time_span, n_steps)
        fin_time2 = time.time()
        final_time2 = fin_time2 - ini_time2

        with open("planeta.csv","a") as archivo:
            archivo.write(formato_datos.format(final_time, final_time2))
