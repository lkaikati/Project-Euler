total = 200
coins=[200,100,50,20,10,5,2,1]
ways=[0]*201
ways[0]=1
for coin in coins:
    for i in range(coin,201):
        ways[i] += ways[i-coin]
print(ways[200])