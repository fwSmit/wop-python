#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

class physicsObject:
    
    def __init__(self):
        self.mass       = 100*1000     # kg
        self.deltaTime 	= 0.1 	#size of the time step (in seconds)
        self.beginTime  = 0 	#start time of simulation (in seconds)
        self.endTime 	= 20 	#end time of simulation (in seconds)
        self.beginPos 	= 0 	#initial position (in meters)
        self.beginVel 	= 10 	#initial velocity (in meters/second)
        self.duration   = self.endTime - self.beginTime
        self.times = np.linspace(self.beginTime, self.endTime, 1+ round((self.duration)/self.deltaTime))
        self.x_an = np.zeros(len(self.times))
        self.v_an = np.zeros(len(self.times))
        self.x_num = np.zeros(len(self.times))
        self.v_num = np.zeros(len(self.times))
        
    
    def getForce(self, v):
        return -100 * v**3; # Newton

    def getAcceleration(self, v):
        a = self.getForce(v)/self.mass
        return a

    def calculateNumerical(self):
        self.x_num[0] = self.beginPos
        self.v_num[0] = self.beginVel
        
        for n in range(len(self.times)-1):
            a = self.getAcceleration(self.v_num[n])
            self.x_num[n+1] = self.x_num[n] + self.v_num[n]*self.deltaTime
            self.v_num[n+1] = self.v_num[n] +  a  * self.deltaTime

    def getVelocityAn(self, t):
        return (200*t/self.mass + 1/100)**-0.5

    def getPositionAn(self, t):
        return self.mass/100 *((1/100 + (200*t)/self.mass)**0.5) - self.mass/1000

    def calculateAnalytical(self):
        for n in range(len(self.times)):
            a = self.getAcceleration(self.times[n])
            self.x_an[n] = self.getPositionAn(self.times[n])
            self.v_an[n] = self.getVelocityAn(self.times[n])
        
    def plotVel(self):
        plt.figure(1)
        plt.plot(self.times, self.v_num)
    
    def plotVelAn(self):
        plt.figure(1)
        plt.plot(self.times, self.v_an, 'y--')
        
    def plotPosition(self):
        plt.figure(0)
        plt.plot(self.times, self.x_num)
        
    def plotPositionAn(self):
        plt.figure(0)
        plt.plot(self.times, self.x_an, 'y--')
        #  plt.plot(t, x_an, 'y--')  #make a yellow dashed line

    def printAnswers(self):
        print(self.v_num[-1])
        print(self.x_num[80])
        #  print(self.getPositionAn(8)-self.x_num[8000])


test = physicsObject()
test.calculateNumerical()
test.calculateAnalytical()
test.printAnswers()
#  test.plotPosition()
#  test.plotPositionAn()
#  test.plotVel()
#  test.plotVelAn()
plt.show()

