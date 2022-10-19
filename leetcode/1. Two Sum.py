class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            key = target - nums[i]
            if key in nums and nums.index(key) != i:
                return [i,nums.index(key)]
