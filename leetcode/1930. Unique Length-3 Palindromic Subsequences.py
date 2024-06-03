class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        left.add(s[0])
        right = {}
        for i in range(2,len(s)):
            right[s[i]] = 1 + right.get(s[i],0)
        
        for j in range(1,len(s)-1):
            for char in left:
                if right.get(char,0):
                    res.add(char+s[j]+char)
            left.add(s[j])
            right[s[j+1]] -=1
        return len(res)
