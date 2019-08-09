import math
import matplotlib.pyplot as plt
import numpy

def T(x):
    pi=math.acos(-1)
    r=abs(math.tan(math.atan(pi*x)))/pi
    return r


def f(x,y,z):                                           #function to be estimated
    r=T(x)+T(3*y)+5*T(z)
    return r

def g(x,y,z,x0,y0,z0):                                  #trilinear interpolating function
    
    r=0.0
    
    i=0
    while (i<d1):                                       
        if (x>x0[i] and  x<=x0[i+1]):                   #pick the x interval
            l=i                                         #define l
            break
        i=i+1
    
    i=0        
    while(i<d2):                                        
        if(y>y0[i] and y<=y0[i+1]):                     #pick the y interval
            m=i                                         #define m
            break
        i=i+1
    
    i=0
    while(i<d3):
        if(z>z0[i] and z<=z0[i+1]):                     #pick the z interval
            n=i                                         #define n
            break
        i=i+1
    d=10**10+0.1                                               
    i=0
    while (i<2):
        j=0
        while (j<2):
            k=0       
            while (k<2):                                
                r=r+(-1)**(i+j+k-1)*(x-x0[l+(i+1)%2])*(y-y0[m+(j+1)%2])*(z-z0[n+(k+1)%2])*f(x0[l+i],y0[m+j],z0[n+k]) 
                dr=((x-x0[l+i])**2 +(y-y0[j+m])**2 +(z-z0[k+n])**2)
                if (d > dr ):
                    d=dr                     #distanza^2 dal punto griglia più vicino
                k=k+1                                   
            j=j+1                                       
        i=i+1
    r=r/((x0[l+1]-x0[l])*(y0[m+1]-y0[m])*(z0[n+1]-z0[n]))
    d=d**(0.5)
    e= abs((f(x,y,z)-r)/(f(x,y,z)+10**(-10)))                                                       #errore relativo
    return d,e
    

d1=10                                                  #no. of divisions of dominium axis
d2=10
d3=10

o1=-0.1                                                    #lower extremum of dominium axis
o2=-0.1
o3=-0.1

s1=10                                                    #upper extremum of dominium axis
s2=10
s3=10

w1=(s1-o1)/d1                                           #interval width
w2=(s2-o2)/d2 
w3=(s3-o3)/d3 

X0=[0]*(d1+1)                                           #the grid 
Y0=[0]*(d2+1) 
Z0=[0]*(d3+1)

i=0
while (i<=d1):
    X0[i]= o1+w1*i
    i=i+1
i=0
while (i<=d2):
    Y0[i]= o2+w2*i
    i=i+1
i=0
while (i<=d3):
    Z0[i]= o3+w3*i
    i=i+1

p=10000                                             #number of random points
a=[0]*(p)
b=[0]*(p)
c=[0]*(p)
er=[0]*(p)
dis=[0]*(p)
j=0


while(j<p):
    a[j]=numpy.random.uniform(low=o1, high=s1, size=None)                   #point to estimate the function in
    b[j]=numpy.random.uniform(o2,s2)     
    c[j]=numpy.random.uniform(o3,s3)  
    er[j]=g(a[j],b[j],c[j],X0,Y0,Z0)[1]
    dis[j]=g(a[j],b[j],c[j],X0,Y0,Z0)[0]
    j=j+1

plt.scatter(dis,er)
plt.title('f(x,y,z)=T(x)+T(3y)+5T(z)')
plt.xlim((w1**2+w2**2+w3**2)**(0.5)*0.01,(w1**2+w2**2+w3**2)**(0.5)*0.5)
plt.ylim(-0.05,1)
plt.xlabel('minimum distance from a grid point')
plt.ylabel('relative error')
plt.show()
