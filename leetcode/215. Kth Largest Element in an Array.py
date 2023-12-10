#Using a heap. It can be easy if you do it using a sort function.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = [-i for i in nums]
        heapq.heapify(lst)

        while k>0:
            res = -heapq.heappop(lst)
            k-=1
        return res
        
#just normal and easy way
#nums.sort()
#return nums[len(nums) - k]
