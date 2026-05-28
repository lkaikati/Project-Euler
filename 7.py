import math
i=2
x=4
while not i == 10001:
    x+=1
    p=1
    for j in range(2,int(math.sqrt(x)+1)):
        if x % j == 0:
            p=0
            break
    if p == 1:
        i+=1
print(x)