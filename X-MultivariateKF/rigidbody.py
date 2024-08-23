
G = 9.81

class RigidBody1D:
	def __init__(self, mass = 0.0):
		self.mass = mass # kg
		self.pos = 0     # meters
		self.vel = 0     # meters/second
		self.acc = 0     # meters/second2

	def iterate(self, fn = 0.0, dt = float):
		# Net Force : Newtons
		# Deltatime : Seconds
		accnow   = (fn  / self.mass) - G
		velnow   = self.vel + (self.acc + accnow) * dt / 2.0
		self.pos = self.pos + (self.vel + velnow) * dt / 2.0
		self.vel = velnow
		self.acc = accnow
