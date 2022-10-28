class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        b = ''.join(x for x in s if x.isalnum()).lower()
        return b == b[::-1]
