#Do the rob either use first element or last element
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        
        def help_rob(nums):
            if len(nums) < 3:
                return max(nums)
            dp = nums
            dp[2] += dp[0]
            for i in range(3,len(dp)):
                dp[i] += max(dp[i-2],dp[i-3])
            return max(dp[-1],dp[-2])
        return max(help_rob(nums[:-1]), help_rob(nums[1:]))
