#Using 2d dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for i in range(amount +1)] for i in range(len(coins)+1)]
        for i in range(len(coins)):
            dp[i][-1] = 1
        
        for i in range(len(coins)-1,-1,-1):
            val = coins[i]
            for j in range(amount-1,-1,-1):
                dp[i][j] = dp[i+1][j]
                if j+val <= amount:
                    dp[i][j] +=  dp[i][j+val]
        return dp[0][0]
