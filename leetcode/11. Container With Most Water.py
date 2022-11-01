class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0 ,len(height)-1
        maxnum = 0
        while r>l:
            if height[l] >= height[r]:
                maxnum = max((r-l) * height[r], maxnum)
                r -=1
            else:
                maxnum = max((r-l) * height[l],maxnum)
                l +=1
        return maxnum
