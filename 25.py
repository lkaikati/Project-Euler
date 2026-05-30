f=[1,1]
while len(str(f[-1]))<1000:
    f.append(f[-2]+f[-1])
    print(len(str(f[-1])))
print(len(f))