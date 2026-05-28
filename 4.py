max=0
for i in range(10,90):
    for j in range(100,999):
        if str(i*j*11) == str(i*j*11)[::-1]:
            if i*j*11>max:
                max=i*j*11
print(max)