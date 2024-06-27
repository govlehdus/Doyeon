class Solution:
    def numSquares(self, n: int) -> int:
        vals = set()
        dp = [n+1] * (n+1)
        for i in range(1,n//2+2):
            if i **2 <=n:
                dp[i**2] = 1
                vals.add(i**2)
        for j in range(1,len(dp)):
            for num in vals:
                if j-num > 0:
                    dp[j] = min(dp[j],1 + dp[j-num])
        return dp[-1] if dp[-1] != n+1 else 0
