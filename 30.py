total = 0
for i in range(2,1000000):
    digits = []
    sum = 0
    for j in str(i):
        digits.append(int(j))
    for j in str(i):
        sum += int(j)**5
    if sum == i:
        total+=i
print(total)