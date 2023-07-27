"""Since I can't use division, i need to make a list of elements multiplication from left to right and right to left, 
so I can multiply the element that is behind me and next to me to get the product of array except self.class 
"""
Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-1,0,-1):
            suf[len(nums)-i] = suf[len(nums)-i-1] * nums[i]
        for i in range(len(nums)):
            res[i] = pre[i] * suf[-(i+1)]
        return res
