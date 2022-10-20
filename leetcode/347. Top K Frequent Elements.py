class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        a = collections.Counter(nums).most_common(k)
        c = []
        for i in range(len(a)):
            c.append(a[i][0])
        return c
