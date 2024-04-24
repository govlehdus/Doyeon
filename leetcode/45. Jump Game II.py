class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        dp = [float('inf')] * len(nums)
        dp[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i+j < len(nums):
                    dp[i] = min(dp[i], 1+ dp[i+j])
        return dp[0]-1
