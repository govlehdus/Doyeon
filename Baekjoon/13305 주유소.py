a = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))
amount = price[0]
cash = 0
for i in range(len(dist)):
    if price[i] < amount:
        amount = price[i]
    cash += dist[i] * amount
print(cash)
