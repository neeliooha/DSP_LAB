import numpy as np
from matplotlib import pyplot as plt
import cmath as c
N=input("enter the number for finding idft:")
X=input('enter seq1:')
p=np.pi
j=c.sqrt(-1)
w=(2*p/N)
x=[]
for n in range(0,N,1):
	sum=0
	for k in range(0,N,1):
		sum=sum+X[k]*np.exp(j*w*n*k)
	x.append(sum/N)
print(x)

