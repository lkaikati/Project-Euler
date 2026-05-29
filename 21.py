def d(x):
    s=0
    for i in range(1,x//2+1):
        if x % i == 0:
            s+=i
    return s
sum_divisors=[0]
for i in range(1,10000):
    sum_divisors.append(d(i))
for i in range(99999):
    sum_divisors.append(0)
print(sum_divisors)
amicables=[]
for i in range(len(sum_divisors)):
    if sum_divisors[sum_divisors[i]] == i and not sum_divisors[i] == i:
        amicables.append(i)
sum=0
for i in amicables:
    sum+=i
print(sum)