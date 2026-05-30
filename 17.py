ones=[0,3,3,5,4,4,3,5,5,4]
tens=[0,0,6,6,5,5,5,7,6,6]
hundreds=[0,13,13,15,14,14,13,15,15,14]
teens=[3,6,6,8,8,7,7,9,8,8]
sum=0
for i in range(1,1000):
    l=0
    if i % 100 < 20 and i % 100 >= 10:
        l+=teens[i%10]
        l+=hundreds[i//100]
    else:
        l+=ones[i%10]
        l+=tens[(i%100)//10]
        l+=hundreds[i//100]
        if i%100==0:
            l-=3
    sum+=l
sum+=11
print(sum)