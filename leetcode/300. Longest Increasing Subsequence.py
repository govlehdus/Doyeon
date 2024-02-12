#Using a dp, do it backward.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(dp)-1,-1,-1):
            for j in range(i+1, len(dp)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+ dp[j])
        return max(dp)
