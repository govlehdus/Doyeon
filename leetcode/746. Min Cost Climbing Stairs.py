class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost + [0]
        for i in range(2,len(dp)):
            dp[i] = dp[i] + min(dp[i-2], dp[i-1])
        return dp[-1]
