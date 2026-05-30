powers=[]
for a in range(2,101):
    for b in range(2,101):
        if not a**b in powers:
            powers.append(a**b)
print(len(powers))