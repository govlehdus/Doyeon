class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s)  for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res +=1
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == True:
                        dp[i][j]= True
                        res +=1
        return res



