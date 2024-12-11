#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Mathematical modeling of motifs

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

###Full model#####

# Decide how to encode your system.
# A State vector [X] is conc. of all the components at a particular time.
# The order in which they are specified needs to remain fixed.
## Here is the example system of an enzymatic reaction:
## Free transcription factor - asnC (Tf)
## Transcription factor and metabolite complex - asnC-aspargine (TfM)
## Enzyme - Asparaginase (E)
## Metabolite - L-aspargine (M)
## Substrate - aspartate (S)
## X0 is the initial state/conditions
# Set initial conditions State vector is [Tf, TfM , E , M , S]

init_state=np.array([10**-1,0,0,0,1]) #µM

# Declare your ODE model in the same order
## dX[0] = dTf/dt, dX[1] = dTfM/dt, dX[2] = dE/dt, dX[3] = dM/dt, dX[4] = dS/dt
def diffEq(X,t):
    # generate a list to store derivatives,
    # The number should be the no. of variables in your system
    dX= np.zeros(5)
    dX[0]= (-k1*X[0]*X[3]) + (k2*X[1]) #-k1*[Tf]*[M]+k2*[TfM]
    dX[1]= (k1*X[0]*X[3]) - (k2*X[1]) #k1*[Tf]*[M]-k2*[TfM]
    dX[2]= (k_syn * (X[0])/(k3+X[0])) -k4*X[2] #(k6*Tf/(k6+Tf))-K7*E #k6 changed to k3 and k7 changed to k4
    dX[3]=((kcat*X[2])*(X[4]/(km+X[4])))-k1*X[0]*X[3]+k2*X[1] #(kcat*E)*([S]/(Km+[S]))-k1*[Tf][M]+k2*[TfM]
    dX[4]=-((kcat*X[2])*(X[4]/(km+X[4]))) #-(kcat*E)*([S]/(Km+[S]))
    return dX

## Tf = X[0]
## TfM = X[1]
## E = X[2]
## M = X[3]
## S = X[4]

#assign parameter values

k1=10**8 #forward binding rate constant for Tf+M--> TfM
k2=10**7 #reverse (unbinding) rate constant for TfM-->Tf+M
k3=10**-1 #dissociation constant of the promoter and transcription factor
k4=0.83 #decay constant of asparagine synthase
kcat=600 #catalytic rate constant of asparaginase
km=3500 #Km michaelis menten constant for the enzymatic reaction
k_syn = 1 #synthesis rate constant of the enzyme

#set time_grid for simulation
t_min=0; t_max=300; dt=0.001
times=np.arange(t_min, t_max+dt, dt) #generate time-grid list

X=odeint(diffEq, init_state, times) #run simulation

# Plot simulation
plt.figure()  # Generate figure
plt.plot(times, X[:, 0], label="Tf (Free asnC)", linewidth=2)  # Free transcription factor conc.
plt.plot(times, X[:, 1], label="TfM (asnC-Aspargine Complex)", linewidth=2)  # Complex conc.
plt.plot(times, X[:, 2], label="E (Aspargine Synthase)", linewidth=2)  # Enzyme conc.
plt.plot(times, X[:, 3], label="M (L-Aspargine)", linewidth=2)  # Metabolite conc.
plt.plot(times, X[:, 4], label="S (Aspartate)", linewidth=2)  # Substrate conc.
plt.xlabel("Time (s)")
plt.ylabel("Concentration (µM)")
plt.legend()
plt.title("Time Evolution of Transcription Factor, Complex, Enzyme, Metabolite, and Substrate")
plt.grid(True)
plt.show()