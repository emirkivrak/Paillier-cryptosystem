from functions import *
import random
from fractions import gcd
from decimal import *



def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def buyuksayidondur_helper():
    while(1):
        a=random.getrandbits(1024)
        if isprime(a):
            return(a)
    

def buyuksayidondur():
    sayilar=[]
    while(1):
        a=buyuksayidondur_helper()
        b=buyuksayidondur_helper()
        if(gcd(a*b,gcd((a-1),(b-1)))==1):
            sayilar.append(a)
            sayilar.append(b)
            return sayilar


def function_L(x,n):
    return (x-1)/n

sayilar=buyuksayidondur()

p=sayilar[0]
q=sayilar[1]
n=p*q
lam=lcm(p-1,q-1)
g=random.randrange(n**2,(n**2)+100)
test=Decimal(1) / Decimal(function_L(pow(g,lam,n**2),n))
#nu=(function_L(pow(g,lam,n**2),n)**-1)%n

print test


print "P===>",p,"\n"
print "Q===>",q,"\n"
print "N===>",n,"\n"
print 'LAMBDA == >'.encode("utf-8"),lam,"\n"
print "G===>",g
#print "NU===>",nu






