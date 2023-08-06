#First change the string to alphanumeric and lower case. Then check with reversed string to find out
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
#Using Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while r>l:    
            while s[l].isalnum() == False and l<r:
                l += 1
            while s[r].isalnum() == False and l<r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l +=1
                r -=1
        return True
