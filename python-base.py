#!/bin/python

import matplotlib.pyplot as plt
import numpy as np


class object:
    mass        = 6     # kg
    deltaTime 	=0.1 	#size of the time step (in seconds)
    beginTime   =0 	#start time of simulation (in seconds)
    endTime 	=10 	#end time of simulation (in seconds)
    beginPos 	=0 	#initial position (in meters)
    beginVel 	=0 	#initial velocity (in meters/second)
    pos = np.array([0, 0])
    vel = np.array([0, 0])
    acc = np.array([0, 0])

    def __init__(self, m, dt, t0, t1, x0, v0):
        self.mass = m
        self.deltaTime = dt
        self.beginTime = t0
        self.endTime = t1
        self.beginPos = x0
        self.beginVel = v0
        
    
    def getForce(t):
        return np.sin(t); # Newton
        
    def graphPos:

    def getAccelleration(t):

        # your code goes here, where acceleration "a" gets calculated
        a = getForce(t)/m
        return a

    

    
    
    


print("test")
dt 	=0.1 	#size of the time step (in seconds)
t0 	=0 	#start time of simulation (in seconds)
t1 	=10 	#end time of simulation (in seconds)
x0 	=0 	#initial position (in meters)
v0 	=0 	#initial velocity (in meters/second)
a       =0
m       = 6     # kg

def acceleration(t):

      # your code goes here, where acceleration "a" gets calculated
      a = np.sin(t)/m
      return a

t = np.linspace(t0, t1, 1+ round((t1-t0)/dt))#, np.round((t1-t0)/dt))
x_an = np.zeros(len(t))
v_an = np.zeros(len(t))


for n in range(len(t)):
    a = acceleration(t[n])
    v_an[n] = - np.cos( t[n] )/m + v0 + np.cos(0)/m
    x_an[n] = - np.sin( t[n] )/m + (v0+np.cos(0)/m)*t[n] + x0



# creating empty arrays for numerical solution

x_num = np.zeros(len(t))
v_num = np.zeros(len(t))

x_num[0] = x0  #initial position
v_num[0] = v0  #initial velocity



for n in range(len(t)-1):
    a = acceleration(t[n])
    x_num[n+1] = x_num[n] + v_num[n]*dt
    v_num[n+1] = v_num[n] +  a  *dt
    #  if dt*n == 8:
        #  print(v_num[n])

#  print(x_num[-1])
#  print(x_num[-1]-x_an[-1])


plt.figure(1)
plt.plot(t, x_num)

plt.plot(t, x_an, 'y--')  #make a yellow dashed line

plt.figure(2)
plt.plot(t, v_num)
plt.plot(t, v_an, 'y--')  #make a yellow dashed line
#  print(acceleration(2));

print(x_num[round( 8./dt )])

#  plt.figure(2)
#  plt.plot(t, x_num-x_an)
plt.show()


