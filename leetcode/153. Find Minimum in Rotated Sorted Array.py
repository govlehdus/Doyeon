#Check the right side of the array(include nums[mid]) and left side. Check if the current position is smallest on the right. Keep minimizing the
#size.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[r]
        while l<=r:
            mid = (l+r)//2

            if nums[mid] <= nums[r]:
                res = min(res,nums[mid])
                r = mid-1
            else:
                l = mid+1
        return res
