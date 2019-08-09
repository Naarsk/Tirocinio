import math                                       #this code generates the 
import numpy                                      #array of values for the
import pickle                                     #interpoolation. run first

def f(x,y,z):                                     #function to be estimated
   r=x*math.exp(-y**2-z**3)*math.cos(math.pi*x)
   return r
 
d=numpy.array([100,100,100])                      #no. of divisions of domain axis
a=numpy.array([0,0,0])                            #lower extremum of domain axis
b=numpy.array([1,1,1])                            #upper extremum of domain axis
w=(b-a)/d                                         #interval width

X0=numpy.zeros(d[0]+1)                            #domain 
Y0=numpy.zeros(d[1]+1) 
Z0=numpy.zeros(d[2]+1)

i=0
while (i<=d[0]):
    X0[i]= a[0]+w[0]*i
    i=i+1
i=0
while (i<=d[1]):
    Y0[i]= a[1]+w[1]*i
    i=i+1
i=0
while (i<=d[2]):
    Z0[i]= a[2]+w[2]*i
    i=i+1
    
Tab = numpy.zeros((d[0]+1,d[1]+1,d[2]+1))        #array of values

i=0
while (i<=d[0]):
    j=0
    while (j<=d[1]):
        k=0
        while (k<=d[2]):
            Tab[i,j,k]=f(X0[i],Y0[j],Z0[k])
            k=k+1
        j=j+1
    i=i+1
    

dat = open('store.pckl', 'wb')
pickle.dump(Tab, dat)
pickle.dump(X0, dat)
pickle.dump(Y0, dat)
pickle.dump(Z0, dat)
pickle.dump(d, dat)
dat.close()
