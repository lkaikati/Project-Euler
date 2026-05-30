import math

def length(x):
    l=0
    a=1
    r=[]
    if not math.gcd(x,10) == 1:
        return 0
    else:
        while True:
            if a%x in r:
                return l
            else:
                r.append(a%x)
                a*=10
                l+=1

maxim=0
m=0
for i in range(1,1000):
    if length(i)>maxim:
        maxim=length(i)
        m=i

print(m)