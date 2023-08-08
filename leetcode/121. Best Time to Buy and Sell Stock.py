"""Since it is getting the smallest value and highest value after getting the smallest value to get the maximum profit, so I choose to keep track of two variables
low and high. Using sliding window algorithm, I updated the low and high when it meets the condition.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,high = float("inf"),0
        res = 0
        for i in prices:
            if i < low:
                low = i
                high = i
            elif i > high:
                high = i
                res = max(res, high-low)
        return res
