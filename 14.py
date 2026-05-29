def collatz(x):
    if x % 2 == 0:
        return x/2
    else:
        return 3*x+1
max=1
maxs=1
for j in range(1,1000000):
    a=j
    i=0
    while not a == 1:
        a = collatz(a)
        i+=1
    if i>maxs:
        maxs=i
        max=j
        print(max,maxs)