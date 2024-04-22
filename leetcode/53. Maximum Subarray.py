class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        val = nums[0]
        for n in nums:
            res += n
            val = max(val, res)
            if res <0:
                res = 0

        return val
