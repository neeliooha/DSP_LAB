import numpy as np
from matplotlib import pyplot as plt
def reverse(h):
	n=len(h)
	y=[]
	for i in range(n):
		s=h[n-1-i]
		y=np.append(y,s)
	return y
def convolute(x,h):
	n1=len(x)
	n2=len(h)
	y=[]
	for n in range(n1+n2-1):
		sum=0
		for k in range(n1):
			if n-k>=0 and n-k<=n2-1:
				sum=sum+(x[k]*h[n-k])
		y=np.append(y,sum)
	return y
x=np.array(input('enter seq1:'))
h=np.array(input('enter seq2:'))
print(convolute(x,reverse(h)))
print('correlation=',np.convolve(x,reverse(h)))
	