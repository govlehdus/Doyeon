#Since I need to iterate one time because it should be O(n)time, so I need to check whether the value is the start of the sequence or not.
#Then if it is the start of the sequence, I check if there is numbers in sequence. 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        for n in nums:
            if (n-1) not in numset:
                length = 1
                while (n+length) in numset:
                    length +=1
                res = max(length, res)
        return res
