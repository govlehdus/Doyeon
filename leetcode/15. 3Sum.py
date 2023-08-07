"""First since it need 3 numbers, sort the list, and iterate it over while having left and right pointer,
so I can check 3 values to know that the sum of the numbers is 0.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            l = i+1
            r = len(nums)-1
            target = 0- nums[i]
            while r>l:
                if nums[r] + nums[l] < target:
                    l +=1
                elif nums[r] + nums[l] > target:
                    r -=1
                else:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                    else:
                        l +=1
        return res
