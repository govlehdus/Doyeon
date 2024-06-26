class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)

        for num in nums:
            if num <= target:
                dp[num] = 1


        for i in range(1, len(dp)):
            for n in nums:
                if i-n > 0 and dp[i - n] :
                    dp[i] += dp[i-n]
        return dp[-1]
