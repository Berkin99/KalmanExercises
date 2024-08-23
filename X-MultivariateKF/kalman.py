
import numpy as np

class Kalman1D:
	def __init__(self, dt = 0.25, sigmax = 0.0, epsilon = 0.0):
		self.dt     = dt
		self.state  = np.array([[0], 
						        [0]])
		self.state1 = np.array([[0], 
						        [0]])
		self.F      = np.array([[1,  dt],
						        [0,   1]])

		self.G      = np.array([[0.5*(dt**2)],
						        [dt         ]])
		
		self.Q      = np.array([[(dt**4)/4 , (dt**3)/2],
						        [(dt**3)/2 , (dt**2)  ]])
		self.Q		= np.dot(self.Q, epsilon**2)

		self.R      = np.array([[sigmax**2]])
		self.I      = np.eye(2)		
		self.H      = np.array([[1, 0]])
		self.Kn     = np.array([[0], 
						        [0]])
		self.Pn     = np.array([[1, 0], 
						        [0, 1]])
		self.Pn1    = np.array([[0, 0], 
						        [0, 0]])
		
		self.stateExtrapolation(0)
		self.covExtrapolation()

	def kalmanGain(self):
		A = np.dot(self.Pn, np.transpose(self.H))
		self.Kn = np.dot(A, np.linalg.inv(np.dot(self.H, A) + self.R))
	
	def stateUpdate(self, zn):
		self.state = self.state1 + np.dot(self.Kn,(zn - np.dot(self.H, self.state1)))

	def covUpdate(self):
		A = self.I - np.dot(self.Kn, self.H)
		self.Pn = np.dot(A, np.dot(self.Pn1, np.transpose(A))) + np.dot(self.Kn, np.dot(self.R, np.transpose(self.Kn)))

	def stateExtrapolation(self, un):
		self.state1 = np.dot(self.F, self.state) + np.dot(self.G, un) 

	def covExtrapolation(self):
		self.Pn1 = np.dot(self.F, np.dot(self.Pn, np.transpose(self.F))) + self.Q
	
	def iterate(self, zn, un):
		self.kalmanGain()
		self.stateUpdate(zn=zn)
		self.covUpdate()
		self.stateExtrapolation(un=un)
		self.covExtrapolation()

