class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        upperLimit = max(nums) + 1 
        store = [0] * upperLimit

        for num in nums:
            store[num] += num

        dp = [0] * upperLimit

        dp[1] =  store[1]
        for i in range(2, upperLimit):
            dp[i] = max(dp[i - 2] + store[i], dp[i - 1])

        return dp[-1]
