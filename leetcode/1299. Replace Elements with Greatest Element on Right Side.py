class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        maxval = arr[-1]
        for i in range(1,len(arr)):
            maxval = max(maxval, arr[-i])
            res.append(maxval)
        return res[::-1]
