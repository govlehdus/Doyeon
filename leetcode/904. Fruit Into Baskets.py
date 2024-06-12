class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l,r = 0,0
        basket = {}
        while r < len(fruits):
            basket[fruits[r]] = 1 + basket.get(fruits[r],0)
            r+=1

            if len(basket) <= 2:
                res = max(res, r-l)
            else:
                while len(basket) >2:
                    basket[fruits[l]] -=1
                    if basket[fruits[l]] == 0:
                        basket.pop(fruits[l])
                    l +=1

            
        return res
