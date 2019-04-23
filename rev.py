import numpy as np
from matplotlib import pyplot as plt
def reverse(h):
	n=len(h)
	y=[]
	for i in range(n):
		s=h[n-1-i]
		y=np.append(y,s)
	return y
h=np.array(input('enter seq:'))
print(reverse(h))
	
