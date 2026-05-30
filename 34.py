import math
total=0
for i in range(3,1000000):
    sum=0
    for j in str(i):
        sum+=math.factorial(int(j))
    if sum==i:
        total+=sum
print(total)