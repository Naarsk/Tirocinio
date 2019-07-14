import math
import matplotlib.pyplot as plt
import numpy

def f(x,y,z):                                        #function to be estimated
   r=x**(1/3)*math.exp(-y**2-z**3)
   return r

def g(x,y,z,x0,y0,z0):                               #trilinear interpolating function
    if(x<x0[0] or x>x0[d1] or y<y0[0] or y>y0[d2] or z<z0[0] or z>z0[d3]):
        print('error: point does not belong to domain',x)
        return 0 
    else:
        r=0.0
        i=0
        while (i<d1):
            if (x>=x0[i] and  x<=x0[i+1]):                #pick the x interval
                l=i                                      #define l
                break
            i=i+1
        
        i=0        
        while(i<d2):                                        
            if(y>=y0[i] and y<=y0[i+1]):                  #pick the y interval
                m=i                                      #define m
                break
            i=i+1
        
        i=0
        while(i<d3):
            if(z>=z0[i] and z<=z0[i+1]):                  #pick the z interval
                n=i                                      #define n
                break
            i=i+1
                                                        
        i=0
        while (i<2):
            j=0
            while (j<2):
                k=0       
                while (k<2):                                
                    r=r+(-1)**(i+j+k-1)*(x-x0[l+(i+1)%2])*(y-y0[m+(j+1)%2])*\
                    (z-z0[n+(k+1)%2])*f(x0[l+i],y0[m+j],z0[n+k]) 
                    k=k+1                                #f values should be tabulated 
                j=j+1                                    #in a list: F[l+i,m+j,n+k]
            i=i+1
        r=r/((x0[l+1]-x0[l])*(y0[m+1]-y0[m])*(z0[n+1]-z0[n]))
        return r
  
a=(0.5,1.00,1.5,2.00,3.00,4.00,5.00,6.00,7.50,9.00) #point to estimate the function in
b=(0.1,0.2,0.45,0.75,0.9,1.00, 1.25,1.50, 1.75,  2.00 )
c=(0.1,0.2,0.45,0.75,0.9,1.00, 1.25,1.50, 1.75, 2.00 )

o1=0                                                 #lower extremum of domain axis
o2=0
o3=0

s1=10                                                 #upper extremum of domain axis
s2=10
s3=10   
 
er=[0]*(100)
div=[0]*(100)

d=1
j=1 
while (j<100):
    d1= d*j
    div[j]=d1
    d2=d1
    d3=d1

    w1=(s1-o1)/d1                                        #interval width
    w2=(s2-o2)/d2 
    w3=(s3-o3)/d3 

    X0=[0]*(d1+1)                                        #the grid 
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
    i=0    
    while (i<10):
        er[j]=er[j]+abs((f(a[i],b[i],c[i])- g(a[i],b[i],c[i],X0,Y0,Z0))/(f(a[i],b[i],c[i])))    
        i=i+1
    
    er[j]=er[j]/10
    print(div[j],er[j]) 
    j=j+1  
     
plt.scatter(div,er)
plt.title('f(x,y,z)=x^(1/3)exp(-y^2-z^2)')
#plt.xlim(-0.5,1000)
plt.ylim(-0.05,11)
plt.xlabel('number of divisions')
plt.ylabel('average relative error')
plt.show()
