from math import *
import matplotlib.pyplot as plt

# physical constants 
A = 0.1        # Amplitude of the road , m
lam = 25       # wave lenght of the road, m 
v = 16.67      # velocity of the car in x-direction, m/s
m = 1500       # mass of the car, kg
k = 80000      # spring constant for suspension, N/m
b = 4000       # Linear damping constant of the suspension, Ns/m

# values
bta = 4/3
omega_0 = 7.3
omega_1 = 7.18
delta = 1.48029

# values
B1 = -0.00906
B2 = -0.10293


t = 0 
dt = 0.01
tmax = 10 

# empty lists
xlist=[]
timelist = []

while t<tmax:
    t = t + dt
    
    #function for car's motion
    x_t = A * cos(omega_1 * t - delta) + exp(-bta*t)* (B1 * cos(omega_1*t) + B2 * sin(omega_1*t))
    
    xlist.append(x_t)
    timelist.append(t)


plt.plot(timelist,xlist, color = "red")
plt.xlabel("x(t)")
plt.ylabel("time")
plt.axhline(y=0, color="black", linestyle='--')
plt.show()


    

    


    
    
    
    