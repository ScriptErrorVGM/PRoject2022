import numpy as np
import pandas as pd


X = np.array([-9.0,-6.0,-3.0,-2.0,4.0,7.0])
p = np.array([0.2,0.2,0.2,0.2,0.1,0.1])

ex = np.dot(X,p)
print(ex) 

dx = np.dot(X**2,p) - np.dot(X,p)**2
print(dx)
