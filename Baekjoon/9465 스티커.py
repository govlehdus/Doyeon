a = int(input())
for i in range(a):
    b = int(input())
    dp = []
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    for i in range(b):
        dp.append([c[i],d[i]])
    if b >=2:
        dp[1][0] += dp[0][1]
        dp[1][1] += dp[0][0]
    for i in range(2,b):
        for j in range(2):
            if j == 0 :
                dp[i][j] = dp[i][j] +max(dp[i-2][1],dp[i-1][1])
            else:
                dp[i][j] = dp[i][j] +max(dp[i-2][0],dp[i-1][0])
    print(max(dp[b-1]))
