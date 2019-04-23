import numpy as np
from matplotlib import pyplot as plt
import cmath as c1
T=0.1
wc=0.35*np.pi
wp=0.7*np.pi
def frequency(wp,wc):	
	ap=((2.0/T)*np.tan(wp/2.0))	
	ast=((2.0/T)*np.tan(wc/2.0))
	return ap,ast
t=frequency(wp,wc)
ap=t[0]
print "analog pass band edge fre=", ap
ast=t[1]
print "analog stop band edge fre=", ast






#order
sp=0.6
ss=0.1
h=ss**2
i=sp**2

def order(h,i,ap,ast):
	x1=((1.0/h)-1.0)
	x2=((1.0/i)-1.0)
	q=(x1/x2)
	k=((1.0/2.0)*np.log(q))
	ap1=1
	ast1=(ap/ast)
	n=np.log(ast1/ap1)
	N=(k/n)
	return N
y=order (h,i,ap,ast)
print y
m=np.abs(y)
n1=np.ceil(m)
print "order=",n1



#cutt off frequency
ss=0.1
def cutof(n1,ss,ast,ap):
	a1=((1.0/ss**2)-1.0)
	a2=(1/(2.0*n1))
	a3=(a1)**a2
	f=((ap/ast)/a3)
	return f
e=cutof(n1,ss,ast,ap)
print "cutt of frequency=",e	


#trasfer function

def trans(e,T,n1):
	bk=2*np.sin((np.pi)/4.0)
	j=c1.sqrt(-1)
	w=np.arange(0,np.pi,0.01)
	z=np.exp(j*w)
	s=((2.0/T)*((1-(1/z))/(1+(1/z))))
	s1=(ap/s)
	p1=((s1**2)+(bk*e*s1)+(e**2))
	p2=e**n1
	hs1=(p2/p1)
	return hs1
h1=trans(e,T,n1)
print"transfer function=",h1
w=np.arange(0,np.pi,0.01)
plt.plot(w,np.abs(h1))
plt.show()














