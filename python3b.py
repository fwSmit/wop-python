#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

#  g = 9.81 # m/s^2
g = 0 # m/s^2

mass            = 12    # kg
deltaTime 	= 0.001 	#size of the time step (in seconds)
beginTime       = 0 	#start time of simulation (in seconds)
endTime 	= 10 	#end time of simulation (in seconds)
beginPos 	= 0.2 	#initial position (in meters)
beginVel 	= 0.6 	#initial velocity (in meters/second)
duration        = endTime - beginTime
times           = np.linspace(beginTime, endTime, 1 + round((duration)/deltaTime))
x_an            = np.zeros(len(times))
v_an            = np.zeros(len(times))
x_num           = np.zeros(len(times))
v_num           = np.zeros(len(times))
spring_k        = 250   # spring stiffness (Newton/meter)
        
# initialize numerical vectors with begin values
x_num[0] = beginPos
v_num[0] = beginVel
        
    
    #  def getForce(self, v):
        #  return -100 * v**3; # Newton

    #  def getAcceleration(self, v):
        #  a = self.getForce(v)/self.mass
        #  return a
    
def derivatives(state, t): #function name is free to choose, but it must take exactly these two inputs
    y = state[0] #this will seem useless for now, but it is best to always unpack your states here
    v = state[1] #same as above, but a little less useless because we will provide v as a return value
    a = - spring_k * y /mass        #you will modify this line several times during this assignment. For now: constant a
    return [v, a]

def getXNum(t):
    return x_num[round(t/deltaTime)]

def calculateNumerical():
    for n in range(len(times)-1):
        afgeleiden = derivatives([x_num[n], v_num[n]], times[n])  #calculate derivatives based on previous state
        # calculate new states based on old states and old derivatives

        # notice how the two states (y and v) are treated exactly the same
        if np.sign(x_num[n-1]) != np.sign( x_num[n] ):
            print("Y is zero")
            print(times[n])

        x_num[n+1] = x_num[n] + afgeleiden[0]*deltaTime
        v_num[n+1] = v_num[n] + afgeleiden[1]*deltaTime 
        

    #  def getVelocityAn(self, t):
        #  return (200*t/self.mass + 1/100)**-0.5

    #  def getPositionAn(self, t):
        #  return self.mass/100 *((1/100 + (200*t)/self.mass)**0.5) - self.mass/1000

    #  def calculateAnalytical(self):
        #  for n in range(len(self.times)):
            #  a = self.getAcceleration(self.times[n])
            #  self.x_an[n] = self.getPositionAn(self.times[n])
            #  self.v_an[n] = self.getVelocityAn(self.times[n])
        
    #  def plotVel(self):
        #  plt.figure(1)
        #  plt.plot(self.times, self.v_num)

    #  def plotVelAn(self):
        #  plt.figure(1)
        #  plt.plot(self.times, self.v_an, 'y--')
        
def plotPosition():
    plt.figure(0)
    plt.plot(times, x_num)
    
def plotPositionAn():
    plt.figure(0)
    plt.plot(times, x_an, 'y--')

def printAnswers():
    print("Answers:")
    print(x_num[-1])
    #  print(self.getPositionAn(8)-self.x_num[8000])


calculateNumerical()
#  calculateAnalytical()
printAnswers()
#  test.plotPosition()
#  test.plotPositionAn()
#  test.plotVel()
#  test.plotVelAn()
plotPosition()
plt.show()

