class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r = 0, k

        res = 0
        temp = 0
        for i in range(k-1):
            if self.isvowel(s[i]):
                temp +=1
        
        for j in range(k-1, len(s)):
            if self.isvowel(s[j]):
                temp +=1
            res = max(res, temp)

            if self.isvowel(s[j-k+1]):
                temp -=1
        return res
    def isvowel(self,s) -> bool:
        if s.lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        return False
