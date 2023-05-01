a = int(input())
dp =[]
for i in range(a):
    dp.append([0]*10)
for i in range(10):
    dp[0][i] = 1
for i in range(1,a):
    for j in range(10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(sum(dp[a-1])%10007)
