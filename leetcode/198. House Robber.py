class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums
        if len(dp) < 3:
            return max(dp)
        dp[2] = dp[2] + dp[0]
        for i in range(3, len(dp)):
            dp[i] = dp[i] + max(dp[i-2], dp[i-3])
        return max(dp[-1], dp[-2])
