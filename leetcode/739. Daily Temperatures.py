#using stack and putting the index and value to the stack, and pop it if the last value is smaller than the current value.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = []
        for i,val in enumerate(temperatures):
            while(stack and stack[-1][1] < val):
                j, va = stack.pop()
                res[j] = i - j
            stack.append([i,val])
        return res
