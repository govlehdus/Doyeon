#Using a heap, and put the distance, x, y and heapify by distance. 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hea = []
        for x,y in points:
            dist = (x**2) + (y**2)
            hea.append((dist, x,y))
        
        heapq.heapify(hea)
        res = []
        while k:
            _,x,y = heapq.heappop(hea)
            res.append((x,y))
            k -= 1
        return res
