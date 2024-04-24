#Using dp
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+3)
        dp[1] = 1
        dp[2] = 1
        if n < 3:
            return dp[n]
        for i in range(3,n+1):
            dp[i] = dp[i-2]+dp[i-1]+dp[i-3]
        return dp[n]
