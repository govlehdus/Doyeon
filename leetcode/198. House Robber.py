class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = nums
        dp[2] += dp[0]
        for i in range(3,len(dp)):
            dp[i] += max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])
