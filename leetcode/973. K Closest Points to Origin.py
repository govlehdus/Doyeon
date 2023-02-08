import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for i in range(len(points)):
            val = math.sqrt(((points[i][0]-0)**2) + ((points[i][1]-0)**2))
            lst.append([val, points[i][0], points[i][1]])
        heapq.heapify(lst)
        res = []
        while k>0:
            v,x,y = heapq.heappop(lst)
            res.append([x,y])
            k -=1
        return res
