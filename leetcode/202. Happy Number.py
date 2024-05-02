class Solution:
    def isHappy(self, n: int) -> bool:
        lst = []
        while n != 1:
            n = str(n)
            newn = 0
            for i in range(len(str(n))):
                newn += int(n[i]) **2
            if newn in lst:
                return False
            else:
                lst.append(newn)
            n = newn
        return True
