from scipy import exp, pi, absolute, linspace
import matplotlib.pyplot as plt

def earth(t):
    return exp(2*pi*1j*t)

def mars(t):
    r = 1.524 # semi-major axis of Mars orbit in AU
    return r*exp(2*pi*1j*(r**-1.5*t))

def distance(t):
    return absolute(earth(t) - mars(t))

x = linspace(0, 20, 1000)
plt.plot(x, distance(x))
plt.xlabel("Time in years")
plt.ylabel("Distance in AU")
plt.ylim(0, 3)
plt.show()