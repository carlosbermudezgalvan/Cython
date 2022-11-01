from math import sqrt

class Planet(objetct):
	def __init__(self):
		#some initial position and velocity
		cdef double self.x = 1.0
		cdef double self.y = 0.0
		cdef double self.z = 0.0
		cdef double self.vx = 0.0
		cdef double self.vy = 0.5
		cdef double self.vz = 0.0
		
		# some mass
		cdef self.m = 1.0

def single_step(Planet planet, double dt):
	"""Make a single time step"""
	
	#Compute force: gravity towards origin
	cdef double distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
	cdef double Fx = -planet.x / distance**3
	cdef double Fy = -planet.y / distance**3
	cdef double Fz = -planet.z / distance**3
	
	# Time step position, acording to velocity
	cdef double planet.x += dt * planet.vx
	cdef double planet.y += dt * planet.vy
	cdef double planet.z += dt * planet.vz
	
	# Time step acording to force and mass
	cdef double planet.vx += dt * Fx /planet.m
	cdef double planet.vy += dt * Fy /planet.m
	cdef double planet.vz += dt * Fz /planet.m
	
def step_time(Planet planet,double time_span,int n_steps):
	"""Make a number of time steps forward"""
	cdef double dt = time_span / n_steps
	cdef int j = 0
	for j in range (n_steps):
		single_step(planet, dt)
