v=3
t=[1,2]
a=[2,0.2]
M=2

def calc_x(v,M,a,t):
    x=[1]*(v+1)
    for n in range(1, v+1):
        suma=0
        for i in range(0,M):
            if n>=t[i]:
                suma+=a[i]*t[i]*x[n-t[i]]
        x[n]=suma/n
    return x
    
def calc_p0(x):
    suma=0;
    for i in x:
        suma+=i
    return 1/suma
    
def calc_pn(x,v,M,a,t):
    p=[1]*(v+1)
    p[0]=calc_p0(x)
    for n in range(1, v+1):
        suma=0
        for i in range(0,M):
            if n>=t[i]:
                suma+=a[i]*t[i]*p[n-t[i]]
        p[n]=suma/n
    return p
    
def calc_bn(P,v,t,i=1):
    suma=0
    for n in range(v-t[i-1]+1,v+1):
        suma+=P[n]
    return suma

def calc_all(v,t,a,M):
    x=calc_x(v,M,a,t)
    p=calc_pn(x,v,M,a,t)
    b1=calc_bn(p,v,t,1)
    b2=calc_bn(p,v,t,2)
    print(x)
    print(p)
    print(b1)
    print(b2)
    
calc_all(v,t,a,M)
    