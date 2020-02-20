#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

class physicsObject:
    #  positions = np.array([0, 0])
    #  velocities = np.array([0, 0])
    #  accellerations = np.array([0, 0])
    def __init__(self):
        self.mass       = 100     # kg
        self.deltaTime 	= 0.1 	#size of the time step (in seconds)
        self.beginTime  = 0 	#start time of simulation (in seconds)
        self.endTime 	= 200 	#end time of simulation (in seconds)
        self.beginPos 	= 0 	#initial position (in meters)
        self.beginVel 	= 5 	#initial velocity (in meters/second)
        self.duration   = self.endTime - self.beginTime
        self.times = np.linspace(self.beginTime, self.endTime, 1+ round((self.duration)/self.deltaTime))
        self.x_an = np.zeros(len(self.times))
        self.v_an = np.zeros(len(self.times))
        self.x_num = np.zeros(len(self.times))
        self.v_num = np.zeros(len(self.times))
        
    
    def getForce(self, t):
        return 12; # Newton

    def getAcceleration(self, t):
        a = self.getForce(t)/self.mass
        return a

    def calculateNumerical(self):
        self.x_num[0] = self.beginPos
        self.v_num[0] = self.beginVel
        
        for n in range(len(self.times)-1):
            a = self.getAcceleration(self.times[n])
            self.x_num[n+1] = self.x_num[n] + self.v_num[n]*self.deltaTime
            self.v_num[n+1] = self.v_num[n] +  a  * self.deltaTime

    def getVelocityAn(self, t):
        return self.getAcceleration(t) * t + self.beginVel

    def getPositionAn(self, t):
        return 0.5*self.getAcceleration(t)*t**2 + self.beginVel*t + self.beginPos

    def calculateAnalytical(self):
        for n in range(len(self.times)):
            a = self.getAcceleration(self.times[n])
            self.x_an[n] = self.getPositionAn(self.times[n])
            self.v_an[n] = self.getVelocityAn(self.times[n])
        
        
    def plotPosition(self):
        plt.figure(0)
        plt.plot(self.times, self.x_num)
        
    def plotPositionAn(self):
        plt.figure(0)
        plt.plot(self.times, self.x_an, 'y--')
        #  plt.plot(t, x_an, 'y--')  #make a yellow dashed line

    def printAnswers(self):
        print(np.interp(3000, self.x_num, self.v_num))
        print(np.interp(2000, self.x_num, self.times))
        print(np.interp(3000, self.x_num, self.times))
        vel = np.interp(3000, self.x_num, self.v_num)
        a = 0.5*self.getAcceleration(0)
        b = self.beginVel
        c = -3000
        d = b**2 - 4 * a * c
        time = (-b + np.sqrt(d))/(2*a)
        time2 = np.interp(3000, self.x_an, self.times)
        error = self.getVelocityAn(time) - vel
        print("vel numerical is: ", vel)
        print("vel ana is: ", self.getVelocityAn(time))
        print("time is ", time)
        print("time 2 is ", time2)
        print("pos at time is ", self.getPositionAn(time2))
        print("error is: ", error)
        #  print(self.getAcceleration(0))
        #  print(self.v_num[-1])
        #  print(self.x_an[-1])
        #  print(self.x_an[-1]-self.x_num[-1])

def vel_int(t):
    return acceleration(t)/4 * t
    #  return -4.7/(m*4)*t**4

def vel_an(t):
    if(t <= 10):
        return acceleration_an(t)/2*t
    else:
        return vel_an(10) - vel_int(10) + vel_int(t)

def pos_int(t):
    return -4.7/(4*5*m)*t**5
    #  return vel_int(t)/5 *t

def pos_an(t):
    if(t <= 10):
        return vel_an(t)/3*t
    else:
        return (pos_an(10) - pos_int(10)) + pos_int(t) + (vel_an(10) - vel_int(10))*(t-10) 


test = physicsObject()
test.calculateNumerical()
test.calculateAnalytical()
test.printAnswers()
test.plotPosition()
test.plotPositionAn()
#  plt.show()

#  for n in range(len(t)):
    #  a = acceleration(t[n])
    #  v_an[n] = vel_an(t[n])
    #  x_an[n] = pos_an(t[n])

    #  #  v_an[n] = - np.cos( t[n] )/m + v0 + np.cos(0)/m
    #  #  x_an[n] = - np.sin( t[n] )/m + (v0+np.cos(0)/m)*t[n] + x0



#  # creating empty arrays for numerical solution

#  x_num = np.zeros(len(t))
#  v_num = np.zeros(len(t))

#  x_num[0] = x0  #initial position
#  v_num[0] = v0  #initial velocity



#  for n in range(len(t)-1):
    #  a = acceleration(t[n])
    #  x_num[n+1] = x_num[n] + v_num[n]*dt
    #  v_num[n+1] = v_num[n] +  a  *dt
    #  #  if dt*n == 8:
        #  #  print(v_num[n])

#  print(x_an[-1])
#  #  print(v_num[-1])
#  #  print(len(t))
#  #  print(x_num[-1]-x_an[-1])


#  plt.figure(1)
#  plt.plot(t, x_num)

#  plt.plot(t, x_an, 'y--')  #make a yellow dashed line

#  plt.figure(2)
#  plt.plot(t, v_num)
#  plt.plot(t, v_an, 'y--')  #make a yellow dashed line
#  #  plt.plot(t, x_num-x_an)
#  plt.show()


