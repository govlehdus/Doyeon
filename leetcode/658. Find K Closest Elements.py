class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, k-1

        while r+1 < len(arr):
            if arr[r+1] - x < x - arr[l]:
                l+=1
                r+=1
            else:
                break
            
        return arr[l:r+1]
