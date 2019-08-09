import math
import numpy
import pickle

def f(x,y,z):                                             #function to be estimated
   r=x*math.exp(-y**2-z**3)*math.cos(math.pi*x)           #unnecessary
   return r

def g(x,y,z,x0,y0,z0,F):                                  #trilinear interpolating function
    if(x<x0[0] or x>x0[d[0]] or y<y0[0] or y>y0[d[1]] or z<z0[0] or z>z0[d[2]]):
        print('error: point does not belong to domain')
        return 0 
    else:
        r=0.0
        i=0
        while (i<d[0]):
            if (x>=x0[i] and  x<=x0[i+1]):                #pick the x interval
                l=i                                       #define l
                break
            i=i+1
        
        i=0        
        while(i<d[1]):                                        
            if(y>=y0[i] and y<=y0[i+1]):                  #pick the y interval
                m=i                                       #define m
                break
            i=i+1
        
        i=0
        while(i<d[2]):
            if(z>=z0[i] and z<=z0[i+1]):                  #pick the z interval
                n=i                                       #define n
                break
            i=i+1
                                                        
        i=0
        while (i<2):
            j=0
            while (j<2):
                k=0       
                while (k<2):                                
                    r=r+(-1)**(i+j+k-1)*(x-x0[l+(i+1)%2])*(y-y0[m+(j+1)%2])*\
                    (z-z0[n+(k+1)%2])*F[l+i,m+j,n+k]
                    k=k+1                                #f values are tabulated 
                j=j+1                                    #in a list (imported)
            i=i+1
        r=r/((x0[l+1]-x0[l])*(y0[m+1]-y0[m])*(z0[n+1]-z0[n]))
        return r

o=[1.00,0.50,0.20]                                       #point to estimate the function in
  
dat = open('store.pckl', 'rb')
Tab = pickle.load(dat)
X0  = pickle.load(dat)
Y0  = pickle.load(dat)
Z0  = pickle.load(dat)
d   = pickle.load(dat)
dat.close()
    
print("real function value:", f(o[0],o[1],o[2]))
print("iterpolated value  :", g(o[0],o[1],o[2],X0,Y0,Z0,Tab))
