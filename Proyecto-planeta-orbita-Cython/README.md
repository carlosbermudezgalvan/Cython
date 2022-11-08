# **Proyecto: Medida de rendimiento cython/python: Problema Planeta en Orbita**
**Autor:**
 Carlos Mario Bermúdez Galván

###**Contexto de experimentación:**

*   Se tiene un archivo orbita_py.py el cual calcula la orbita de un planeta dado sus argumentos.
*   Se adapto el archivo .py a Cython para mejorar su rendimiento
*   Se creó un archivo principal.py donde se ejecutaron ambos programas con los mismos parametros (planeta tierra), Los argumentos necesarios fueron tomados de Wikipedia.
*   En principal.py se formatean los datos que arrojan los programas (tiempos de ejecución) para posteriormente realizar la comparativa de rendimiento).

###**Pasos para replicar o llevar a cabo la ejecución**
*   Primeramente se clona el repositorio o se descarga el ZIP, en caso de descargar el ZIP descomprimirlo en un directorio exclusivamente para ello.

*   Abrir la consola de su distribución de Linux y entrar al directorio donde se extrajeron los archivos.

*   Escribir el comando :    make all     , el cual permitirá ejecutar posteriormente las funciones del archivo cython.
*   Para ejecutar el test, simplemente ejecutar el archivo principal.py mediante el siguiente comando:       python3 principal.py

**Nota:** Es necesario instalar los paquetes de cython3, pyhton3, gcc, build-essential y make. Para ellos consultar en la web la instalación de cada uno dependiendo de su distribución de Linux.
