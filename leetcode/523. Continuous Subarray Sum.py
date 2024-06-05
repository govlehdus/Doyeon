class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        vals = {0:-1}
        modu = 0
        for i in range(len(nums)):
            modu += nums[i]
            modu %= k
            
            if modu not in vals:
                vals[modu] = i
            elif i - vals[modu] >= 2:
                return True
            
        return False
