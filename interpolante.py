import math
def f(x,y,z):
   r=x*math.exp(-x**2-y**2-z**2)
   return r

def g(x,y,z,x0,y0,z0):
    r=0.0
    i=0
    l=0
    while (l<100):#per ora con l cosi si trovano solo i punti (a,a,a) sulla diagonale del cubo-dominio, sistema poi con piu indici indipendenti l,m,
        if (x>x0[l] and y>y0[l] and z>z0[l] and x<=x0[l+1] and y<=y0[l+1] and z<=z0[l+1]):
            i=0
            while (i<2):
                j=0
                while (j<2):
                    k=0       
                    while (k<2):        
                        r=r+(-1)**(i+j+k-1)*(x-x0[l+abs(i-1)])*(y-y0[l+abs(j-1)])*(z-z0[l+abs(k-1)])*f(x0[l+i],y0[l+j],z0[l+k])
                        k=k+1
                    j=j+1
                i=i+1
            r=r/((x0[l+1]-x0[l])*(y0[l+1]-y0[l])*(z0[l+1]-z0[l]))
        l=l+1
    return r1

X0=[0]*101
Y0=[0]*101    
Z0=[0]*101

l=0
while (l<101):
    X0[l]= -2+l*0.04
    Y0[l]= -2+l*0.04 #l to m
    Z0[l]= -2+l*0.04 #l to n
    l=l+1

l=0
while (l<101):
    a=0.285+0.005*l
  #  print(f(a,a,a))
  #  print(g(a,a,a,X0,Y0,Z0))
    print(100*abs(f(a,a,a)-g(a,a,a,X0,Y0,Z0))/f(a,a,a),"%")
    l=l+1
