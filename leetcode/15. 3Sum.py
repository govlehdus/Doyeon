class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            l,r = i+1,len(nums)-1
            while r>l:
                added = nums[r] + nums[l]
                if added >target:
                    r -= 1
                elif added < target:
                    l += 1
                else:
                    if [nums[i],nums[l],nums[r]] in lst:
                        l +=1
                        
                    else:
                        lst.append([nums[i],nums[l],nums[r]])
                        l +=1
                        
        return lst
