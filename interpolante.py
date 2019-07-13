import math

def f(x,y,z):                                        #function to be estimated
   r=x*math.exp(-y**2-z**3)*math.cos(math.pi*x)
   return r

def g(x,y,z,x0,y0,z0):                               #trilinear interpolating function
    if(x<x0[0] or x>x0[d1] or y<y0[0] or y>y0[d2] or z<z0[0] or z>z0[d3]):
        print('error: point does not belong to domain')
        return 0 
    else:
        r=0.0
        i=0
        while (i<d1):
            if (x>=x0[i] and  x<=x0[i+1]):                #pick the x interval
                l=i                                       #define l
                break
            i=i+1
        
        i=0        
        while(i<d2):                                        
            if(y>=y0[i] and y<=y0[i+1]):                  #pick the y interval
                m=i                                       #define m
                break
            i=i+1
        
        i=0
        while(i<d3):
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
                    (z-z0[n+(k+1)%2])*f(x0[l+i],y0[m+j],z0[n+k]) 
                    k=k+1                                #f values should be tabulated 
                j=j+1                                    #in a list: F[l+i,m+j,n+k]
            i=i+1
        r=r/((x0[l+1]-x0[l])*(y0[m+1]-y0[m])*(z0[n+1]-z0[n]))
        return r
  
a=1.00                                               #point to estimate the function in
b=0.00
c=0.00

d1=1000                                              #no. of divisions of domain axis
d2=1000
d3=1000

o1=0                                                 #lower extremum of domain axis
o2=0
o3=0

s1=1                                                 #upper extremum of domain axis
s2=1
s3=1

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
    
print("real function value:", f(a,b,c))
print("iterpolated value:", g(a,b,c,X0,Y0,Z0))
#print("percentage error:", round(100*abs((f(a,b,c)-g(a,b,c,X0,Y0,Z0))/f(a,b,c)),2),"%")
