class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dic = {}
        for w,h in rectangles:
            dic[w/h] = 1 + dic.get(w/h,0)
        res = 0
        for v in dic.values():
            res += (v * (v-1))/ 2
        return int(res)
