sqsum=0
sum=0
for i in range(1,101):
    sum+=i
for i in range(1,101):
    sqsum+=i**2
print(sum**2-sqsum)