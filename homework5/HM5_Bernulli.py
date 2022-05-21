import scipy.stats as st
from math import factorial 
import scipy.special as sp
import matplotlib.pyplot as plt 
import numpy as np


# number 3

A = st.binom(n=4, p=0.4)
res_A = A.pmf(3) + A.pmf(4)
print(res_A)
x = np.arange(0, 5)
prob = st.binom.pmf(x,4,0.4)
plt.vlines(x,0,prob,colors='purple',lw=5,alpha=0.5)
plt.show()

B = st.binom(n=5, p=0.8)
res_B = B.pmf(4) + B.pmf(5)
print(res_B)
x = np.arange(0, 6)
prob = st.binom.pmf(x,5,0.8)
plt.vlines(x,0,prob,colors='purple',lw=5,alpha=0.5)
plt.show()


# number 12

X = st.binom(n=4, p=0.6)
res_X = X.pmf(2)
print(res_X)
x = np.arange(0, 5)
prob = st.binom.pmf(x,4,0.6)
plt.vlines(x,0,prob,colors='purple',lw=5,alpha=0.5)
plt.show()

res_X_2 = X.pmf(3)
print(res_X_2)



