class Solution:
    def minSwaps(self, s: str) -> int:
        check = 0
        unbalanced = 0
        for i in s:
            if i == "]":
                unbalanced +=1
            else:
                unbalanced -=1
            check = max(check, unbalanced)
        return (check +1 )//2
