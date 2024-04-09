#Used 2d dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(len(prices)+2)] for j in range(len(prices)+2)]
        res = 0
        for i in range(2, len(prices)+2):
            for j in range(i+1, len(prices)+2):
                if prices[i-2] < prices[j-2]:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j], (prices[j-2]-prices[i-2])+dp[i-3][i-2])
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return res
