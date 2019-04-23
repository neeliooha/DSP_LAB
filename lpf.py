#lpf using butterworth approximation
import numpy as np 
import matplotlib.pyplot as plt
import cmath as c1
T=0.1
wp=0.35*np.pi
ws=0.7*np.pi
def frequency(wp,ws):
	a=((2.0/T)*np.tan(wp/2.0))
	b=((2.0/T)*np.tan(ws/2.0))
	return(a,b)
t=frequency(wp,ws)
p=t[0]
print "pass band frequency:",p
q=t[1]
print "stop band frequency:",q


#order

dp=0.6
ds=0.1
x1=dp**2
x2=ds**2
def order(x1,x2,p,q):
	m=((1.0/x2)-1.0)
	n=((1.0/x1)-1.0)
	x=m/n
	y=np.sqrt(x)
	z=np.log(y)
	r=np.log(q/p)
	N=z/r
	return N
y=order(x1,x2,p,q)
print y
N1=np.ceil(y)	
print "order=",N1


#cut off freuency

ds=0.1
def cutoff(N1,ds,q):
	a1=((1.0/ds**2)-1.0) 
	a2=(1/(2.0*N1))
	a3=(a1)**a2
	f=(q/a3)
	return f
cf=cutoff(N1,ds,q)
print "cutoff frequency=",cf

#FINDING bk

k=N1/2.0
bk=2*np.sin(((2*k-1)*np.pi)/(2*N1))
print "bk:",bk


#finding transfer function
bk=2*np.sin(((2*k-1)*np.pi)/(2*N1))
def transfer(cf,N1,bk):
	w=np.arange(0,np.pi,0.1)
	j=c1.sqrt(-1)
	z=np.exp(j*w)
	s=(2/T)*(1-(1/z))/(1+(1/z))
	b2=(s**2)+(bk*cf*s)+(cf**2)
	b3=(cf**N1)
	h=b3/b2
	return h
h1=transfer(cf,N1,bk)
#print"tranfer function",h1
w=np.arange(0,np.pi,0.1)
plt.plot(w,np.abs(h1))
plt.show()

	



	



	



