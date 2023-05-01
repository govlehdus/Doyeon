a= int(input())
b = list(map(int,input().split()))
dp = [1] * a
for i in range(a):
    for j in range(i):
        if b[i] >b[j] and dp[j] == dp[i]:
            dp[i] +=1
print(max(dp))
