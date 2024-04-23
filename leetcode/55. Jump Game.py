class Solution:
    def canJump(self, nums):
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums)-2,-1,-1):
            for j in range(1, nums[i]+1):
                if dp[i+j] == True:
                    dp[i] = True
                    break
        return dp[0]
