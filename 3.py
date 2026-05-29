x=600851475143
y=0
i=3
while not x==1:
    if x % i == 0:
        x/=i
        y=i
    else:
        i+=2
print(y)
