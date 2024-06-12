class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        l,r =0,0
        curr = 0
        while r <len(nums):
            curr += nums[r]
            r +=1
            while curr >= target:
                res = min(res, r-l)
                curr -= nums[l]
                l +=1
            
        return res
