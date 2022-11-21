#Medida de rendimiento cython/python:
Autor:
 Carlos Mario Bermúdez Galván

##Contexto de experimentación:

*   Se requiere comparar el rendimiendo de dos algoritmos en dos lenguajes de programación: Cython y Python.
*   Para ello se escogieron dos algoritmos de ordenamiento, bubble sort y el merge sort.
*   Ambos algoritmos se escogieron debido a que poseen distinta complejidad, sin embargo, ambos realizan lo mismo debido a que como su nombre lo indica son algoritmos de ordenamiento.
*   En el presente notebook se presentará el análisis y comparación de rendimiento de un algoritmo y luego del otro.
*   El resumen del procedimiento sería programar el algoritmo primeramente en python (archivo.py), luego convertirlo a lenguaje Cython (archivo.pyx).
*   Luego crear un archivo main.py (en el presente caso se llamó principal.py), en donde se ejecutará el algoritmo en ambos lenguaje y se registraran los tiempos de ejecución en un archivo .csv
*   Sin embargo antes de ejecutar el experimento (principal.py), debe compilarse el archivo .pyx (Cython), para ello es necesario el MakeFile y el setup.py.

###Pasos para replicar o llevar a cabo la ejecución
*   Primeramente se clona el repositorio o se descarga el ZIP, en caso de descargar el ZIP descomprimirlo en un directorio exclusivamente para ello.

*   Abrir la consola de su distribución de Linux y entrar al directorio donde se extrajeron los archivos.

*   Escribir el comando :    make all     , el cual permitirá ejecutar posteriormente las funciones del archivo cython.
*   Para ejecutar el test, simplemente ejecutar el archivo principal.py mediante el siguiente comando:       python3 principal.py

Nota: Es necesario instalar los paquetes de cython3, pyhton3, gcc, build-essential y make. Para ellos consultar en la web la instalación de cada uno dependiendo de su distribución de Linux.






