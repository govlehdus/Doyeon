#using binary search, keep on checking it. Put the return mid into else, since it is the least thing to happen.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 ,len(nums)-1
        while left<= right:
            mid = left + ((right-left)//2) #if i do (left + right)//2, it can lead to overflow.
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] <target:
                left = mid +1
            else:
                return mid
        return -1
        
