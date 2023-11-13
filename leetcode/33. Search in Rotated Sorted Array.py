#using binary search since it is O(log(n)) time complexity. Having a left portion or right portion, do the algorithm

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        
        return -1
