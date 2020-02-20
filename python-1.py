#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

print("test")
dt 	=0.1 	#size of the time step (in seconds)
t0 	=0 	#start time of simulation (in seconds)
t1 	=10 	#end time of simulation (in seconds)
x0 	=0 	#initial position (in meters)
v0 	=4 	#initial velocity (in meters/second)
a = 0

t = np.linspace(t0, t1, 1+ round((t1-t0)/dt))#, np.round((t1-t0)/dt))
print(t);
x_an = np.zeros(len(t))
v_an = np.zeros(len(t))


for n in range(len(t)):
    v_an[n] = v0 + a*t[n]
    x_an[n] = x0 + v0*t[n] + 0.5*a*t[n]**2



# creating empty arrays for numerical solution

x_num = np.zeros(len(t))
v_num = np.zeros(len(t))

x_num[0] = x0  #initial position
v_num[0] = v0  #initial velocity



for n in range(len(t)-1):
    a = 0

    x_num[n+1] = x_num[n] + v_num[n]*dt
    v_num[n+1] = v_num[n] +  a  *dt
    if dt*n == 8:
        print(v_num[n])

print(x_num[-1])
plt.figure(1)
plt.plot(t, x_num)

plt.plot(t, x_an, 'y--')  #make a yellow dashed line


plt.figure(2)
plt.plot(t, x_num-x_an)
plt.show()

