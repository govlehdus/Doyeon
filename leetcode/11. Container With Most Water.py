"""Using two pointers, I will have left and right pointers, and by moving left or right pointers one, check the maximum container.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        while r>l:
            if height[l] > height[r]:
                count = min(height[l], height[r]) * (r-l)
                res = max(res,count)
                r -=1
            else:
                count = min(height[l], height[r]) * (r-l)
                res = max(res,count)
                l +=1
        return res
