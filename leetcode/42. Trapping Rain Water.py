class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        result = 0
        while r>l:
            if height[r] > height[l]:
                if height[l] < lmax:
                    result += lmax-height[l]
                    l+=1
                else:
                    lmax = height[l]
                    l+=1
            else:
                if rmax > height[r]:
                    result += rmax - height[r]
                    r -=1
                else:
                    rmax = height[r]
                    r -=1
        return result
