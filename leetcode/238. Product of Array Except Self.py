class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]
        b=[1]
        
        ans = []
        for i in range(1, len(nums)):
            a.append(nums[i-1]*a[i-1])
            b.append(nums[-i] * b[i-1])
        for j in range(len(nums)):
            ans.append(a[j] * b[-1-j])
        return ans
