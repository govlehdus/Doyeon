class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lst = []
        for i in range(len(costs)):
            val = abs(costs[i][0] - costs[i][1])
            lst.append([val,(costs[i][0],costs[i][1])])
        lst = sorted(lst, reverse=True)
        a_count, b_count = len(costs)//2 , len(costs)//2
        res = 0
        i = 0
        while a_count and b_count:
            
            if lst[i][1][0] < lst[i][1][1]:
                res += lst[i][1][0]
                a_count -=1
                i+=1
            else:
                res += lst[i][1][1]
                b_count -=1
                i+=1
        if a_count:
            for i in range(1, a_count +1):
                res += lst[-i][1][0]
        if b_count:
            for i in range(1, b_count +1):
                res += lst[-i][1][1]
        return res
