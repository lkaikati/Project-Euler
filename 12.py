import math
a=0
d=0
max=0
while d<250:
    a+=1
    x=a*(a+1)//2
    divisors=[1]
    i=2
    while math.sqrt(x)>=i:
        if x % i == 0:
            divisors.append(i)
        i+=1
    d=len(divisors)
    if d>75:
        print(d)
print(x)