class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums)+1)
        dp[0] = True
        for i in range(1, len(nums)):
            if i <2:
                if nums[i] == nums[i-1] and dp[i-1]:
                    dp[i+1] = True
            else:
                if nums[i] == nums[i-1] and dp[i-1]:
                    dp[i+1] = True
                elif nums[i] == nums[i-1] and nums[i] == nums[i-2] and dp[i-2]:
                    dp[i+1] = True
                elif nums[i] == nums[i-1]+1 and nums[i] == nums[i-2]+2 and dp[i-2]:
                    dp[i+1] = True
        return dp[-1]
