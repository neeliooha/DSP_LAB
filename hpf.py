#hpf using butterworth approximation
import numpy as np 
import matplotlib.pyplot as plt
import cmath as c1
T=0.1
wp=0.7*np.pi
ws=0.35*np.pi
def frequency(wp,ws):
	ap=((2.0/T)*np.tan(wp/2.0))
	ast=((2.0/T)*np.tan(ws/2.0))
	return(ap,ast)
t=frequency(wp,ws)
ap=t[0]
print "pass band frequency:",ap
ast=t[1]
print "stop band frequency:",ast

#order
adp=0.6
ads=0.1
x1=adp**2
x2=ads**2
app=1
astt=ap/ast
def order(x1,x2,app,ast):
	m=((1.0/x1)-1.0)
	n=((1.0/x2)-1.0)
	x=m/n
	y=np.sqrt(x)
	z=np.log(y)
	r=np.log(app/ast)
	N=z/r
	return N
y=order(x1,x2,app,ast)
print y
N1=np.ceil(y)	
print "order=",N1






	



	



