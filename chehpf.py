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
ss=0.1
sp=0.6
h=ss**2
i=sp**2
def order(ap,ast,h,i):
	x1=((1.0/h)-1.0)
	x2=((1.0/i)-1.0)
	q=(x1/x2)
	p1=c1.sqrt(q)
	a1=np.arccosh(p1)
	ast1=(ap/ast)
	ap1=(ap/ap)
	a2=np.arccosh((ast1/ap1))
	N=(a1/a2)
	return N
y=order(ap,ast,h,i)
m=np.abs(y)
n1=np.ceil(m)
print "order=",n1



#transfer  function
def trans(n1,ap,T):
	sp=0.6
	ap1=(ap/ap)
	ep=((sp**-2.0)-1.0)
	ep1=c1.sqrt(ep)
	#print ep1
	x1=(1.0+(1.0/ep))
	x2=c1.sqrt(x1)
	#print x2
	x3=(x2+(1.0/ep1))
	#print x3
	y1=((x3**(1.0/n1)))
	#print y1
	y2=(x3**(-1/n1))
	#print y2
	yn=((1.0/2.0)*(y1-y2))
	print yn
	y3=np.cos(np.pi/(2.0*n1))
	#print y3
	ck1=yn**2
	#print ck1
	ck2=y3**2
	#print ck2
	ck=(ck1+ck2)
	#print ck
	bk=2.0*yn*np.sin((np.pi/(2.0*n1)))
	#print bk
	m1=(1.0/c1.sqrt(1.0+ep))
	h1=(m1*(ap1**n1)*ck)
	j=c1.sqrt(-1)
	w=np.arange(0,np.pi,0.01)
	z=np.exp(j*w)
	s=((2.0/T)*((1.0-(1.0/z))/(1.0+(1.0/z))))
	s1=(ap/s)
	h2=((s1**2.0)+(bk*ap1*s1)+((ap1**2.0)*ck))
	hs=(h1/h2)
	return hs
hs1=trans(n1,ap,T)
w=np.arange(0,np.pi,0.01)
plt.plot(w,np.abs(hs1))
plt.show()
	
