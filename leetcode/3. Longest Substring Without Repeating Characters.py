"""To measure the longest substring, I use sliding window algorithm to put the max substrings and remove the first element until it is the same as new element to put.
To do that fast, I choose to build a deque which is first in first out, so it is fast to pop the first element"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = collections.deque()
        res = 0
        for i in s:
            if i not in q:
                q.append(i)
            else:
                while i in q:
                    q.popleft()
                q.append(i)
            res = max(res, len(q))
        return res
#In a shorter code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = collections.deque()
        res = 0
        for i in s:
            while i in q:
                q.popleft()
            q.append(i)
            res = max(res, len(q))
        return res
            
