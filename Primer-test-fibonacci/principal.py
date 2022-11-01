import fib_cy
import fib_py
import time

ini_time = time.time()
fib_cy.fib_cy(555)
fin_time = time.time()

cython_time = fin_time - ini_time

ini_time = time.time()
fib_py.fib_py(555)
fin_time = time.time()

python_time = fin_time - ini_time

print("Cython= ", cython_time," seg")
print("Python= ", python_time," seg")
print(" es " , python_time/cython_time, " mas rapido")
