class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, cnt = 0,0
        string = ''
        for i in s:
            if i not in string:
                string += i
                cnt = max(cnt, len(string))
            else:
                while string[0] != i :
                    string = string[1:]
                string = string[1:]
                string += i
        return cnt
