#!/bin/python

import matplotlib.pyplot as plt
import numpy as np


dt 	=0.1 	#size of the time step (in seconds)
t0 	=0 	#start time of simulation (in seconds)
t1 	=20 	#end time of simulation (in seconds)
x0 	=0 	#initial position (in meters)
v0 	=0 	#initial velocity (in meters/second)
a       =0
m       = 6     # kg

def force(t):
    if(t < 10):
        return 3.5*t
    else:
        return -4.7 * t**3

def force_an(t):
    if(t <= 10):
        return 3.5*t
    else:
        return -4.7 * t**3

def acceleration_an(t):
      a = force_an(t)/m
      return a

def acceleration(t):
      a = force(t)/m
      return a

t = np.linspace(t0, t1, 1+ round((t1-t0)/dt))#, np.round((t1-t0)/dt))
x_an = np.zeros(len(t))
v_an = np.zeros(len(t))


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

for n in range(len(t)):
    a = acceleration(t[n])
    v_an[n] = vel_an(t[n])
    x_an[n] = pos_an(t[n])
    
    #  v_an[n] = - np.cos( t[n] )/m + v0 + np.cos(0)/m
    #  x_an[n] = - np.sin( t[n] )/m + (v0+np.cos(0)/m)*t[n] + x0



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

print(x_an[-1])
#  print(v_num[-1])
#  print(len(t))
#  print(x_num[-1]-x_an[-1])


plt.figure(1)
plt.plot(t, x_num)

plt.plot(t, x_an, 'y--')  #make a yellow dashed line

plt.figure(2)
plt.plot(t, v_num)
plt.plot(t, v_an, 'y--')  #make a yellow dashed line
#  plt.plot(t, x_num-x_an)
plt.show()


