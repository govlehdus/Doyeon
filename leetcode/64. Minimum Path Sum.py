class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[float('inf') for i in range(col+1)] for j in range(row+1)]
        dp[row][col-1] = 0
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
