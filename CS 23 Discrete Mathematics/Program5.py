
import math



def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
def phi(a):
    b=a-1
    c=0
    while b:
        if not gcd(a,b)-1:
            c+=1
        b-=1
    return c



def power(a,b,c):
    if(b==1):
        return a%c
    x = power(a,b>>1,c)
    x = (x*x)%c
    if(b&1==1)==1: # if odd number
        x = (x*a)%c
    return x


def invmodp(a, p):
    
    for d in xrange(1, p):
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d



n = 3233
e = 17
c = 2790


s = phi(n)
d = invmodp(e,s) 
m = power(c,d,n)

print (m)


 

