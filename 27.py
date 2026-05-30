import math

def primes(b,c):
    p=True
    primes=0
    while p:
        fx=primes**2+b*primes+c
        if fx<0:
            return primes
        for i in range(2,int(fx**0.5)+1):
            if fx%i==0:
                return primes
        primes+=1

max=0
product=0

for i in range(-1000,1001):
    for j in range(1,1001):
        a=primes(i,j)
        if a>max:
            max=a
            product=i*j
            print(max)

print(product)