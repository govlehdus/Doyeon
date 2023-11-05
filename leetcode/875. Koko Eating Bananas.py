#it is finding a number from 0 to the maximum number of the piles, so using binary search, we can find it.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l <=r:
            totaltime = 0
            mid = (l+r)//2

            for p in piles:
                totaltime += ceil(p/mid)
            
            if totaltime <= h:
                res = mid
                r = mid-1
            else:
                l = mid +1
        return res
