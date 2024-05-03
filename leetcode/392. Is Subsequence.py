class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        val = t.find(s[0])
        for char in s:
            if char not in t:
                return False
            val = t.find(char)
            t = t[val+1:]
            
        return True
