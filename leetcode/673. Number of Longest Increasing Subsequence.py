class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
            
        dp = {}
        lenlis, res = 0,0

        for i in range(len(nums)-1,-1,-1):
            maxLen, maxCnt = 1,1

            for j in range(i +1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length +1 > maxLen:
                        maxLen, maxCnt = length +1 , count
                    elif length +1 == maxLen:
                        maxCnt += count
            if maxLen > lenlis:
                lenlis, res = maxLen , maxCnt
            elif lenlis== maxLen:
                res += maxCnt
            
            dp[i] = [maxLen, maxCnt]

        return res
