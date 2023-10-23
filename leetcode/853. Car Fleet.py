#using a stack
#making a list that reverse sort so that the further position is coming to the first and measure the time it takes to the target and pop it
#if it is less than the further one that makes a fleet.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [(p,s) for p,s in zip(position, speed)]
        res = []
        lst.sort(reverse=True)

        for p,s in lst:
            res.append((target - p) /s)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)
