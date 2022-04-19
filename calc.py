import numpy as np

def derivative(x,y):
    return (y[1:]-y[:1])/(x[1]-x[0])
