sum=0
prime = [True] * 2000000
for p in range(2,2000000):
    if prime[p]:
        sum+=p
        for i in range(p*2,2000000,p):
            prime[i]=False
print(sum)