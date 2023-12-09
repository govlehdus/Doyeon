#Using a heap and put the - for the values to use it as a max heap.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-i for i in stones]
        heapq.heapify(lst)
        while len(lst) > 1:
            x = heapq.heappop(lst)
            y = heapq.heappop(lst)

            if x !=y:
                x = x-y
                heapq.heappush(lst, x)
        lst.append(0)
        return abs(lst[0])
