import math

def divisors(x):
    out=[1]
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            out.append(i)
            if not i==math.sqrt(x):
                out.append(x/i)
    return out

def sum_div(x):
    sum=0
    d=divisors(x)
    for i in range(0,len(d)):
        sum+=d[i]
    return sum

abundants=[]

for i in range(1,28124):
    if sum_div(i)>i:
        abundants.append(i)

set=set(abundants)

def summable(x):
    for i in set:
        if i>x:
            break
        if x-i in set:
            return True
    return False

sum=0

for i in range(1,28124):
    if not summable(i):
        sum+=i
print(sum)