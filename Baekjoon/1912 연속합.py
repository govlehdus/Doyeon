a= int(input())
b = list(map(int,input().split()))
dp = [0] * a
for i in range(a):
    dp[i] = max(dp[i-1]+b[i], b[i])
print(max(dp))
