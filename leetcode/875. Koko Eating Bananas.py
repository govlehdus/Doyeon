import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = max(piles)
        while l <= r:
            m = (l+r)//2
            res = 0
            for p in piles:
                res += math.ceil(p / m)
            if res <= h:
                ans = min(m,ans)
                r = m - 1
            else:
                l = m  +1 
        return ans
