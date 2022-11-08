# Fecha: Noviembre - 2022
# Autor: Carlos Bermudez
# Materia: Computación paralela y distribuida
# Temas: Cython vs Python comparativa rendimiento
#------------------------------------------------------------
# Archivo Cython resultando de la conversión de orbite_py.py
# a cython (orbita_cy.pyx), para ser ejecutar y posteriormente
# comparar su tiempo de ejecucion con el archivo .py.
#------------------------------------------------------------
# NOTA: orbita_cy y orbite_py reciben los mismos argumentos
#       necesarios para su ejecucion
#------------------------------------------------------------

#cython: language_level=3
#from libc.math cimport sqrt
"""
    Se requiere la raiz cuadrada
        - Se instancia como función entera
        - Se prepara para multihilo
"""
cdef extern from "math.h":
    double sqrt(double x) nogil
    
cdef class Planet(object):
    cdef public float x,y,z,vx,vy,vz,m
    def __init__(self):
        #some initial position and velocity
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0

        # some mass
        self.m=1.0

"""
Puede ser la distancia 0:
Para evitar lo anterior, se prepara una alerta
basada en Cython: cdivision[True/False]:
        SI es True, invalida la instruccion al saltar la bandera
Se prepara con un decorador de CYTHON
"""
cimport cython
@cython.cdivision(True)
cdef void single_step(Planet planet, double dt) nogil:
    """Make a single time step"""
    #Compute force: gravity towards origin
    cdef double distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    cdef double Fx= -planet.x/distance**3
    cdef double Fy= -planet.y/distance**3
    cdef double Fz= -planet.z/distance**3

    #Time step position, according to velocity
    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    #Time step velocity, according to force and mass
    planet.vx += dt * Fx / planet.m
    planet.vy += dt * Fy / planet.m
    planet.vz += dt * Fz / planet.m
    
def step_time(Planet planet, double time_span, int n_steps):
    """Make a number of time steps forward"""
    cdef int j
    cdef double dt = time_span / n_steps
    """
    Se prepara para paralelismo
    """
    with nogil:
            for j in range (n_steps):
                single_step(planet, dt)
