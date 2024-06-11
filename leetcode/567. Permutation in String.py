class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic1 = {}
        dic2 = {}

        for let in s1:
            dic1[let] = 1+ dic1.get(let,0)
        
        for i in range(len(s1)-1):
            dic2[s2[i]] = 1 + dic2.get(s2[i],0)
        
        for j in range(len(s1)-1,len(s2)):
            dic2[s2[j]] = 1 + dic2.get(s2[j],0)
            if dic1 == dic2:
                return True
            
            dic2[s2[j-len(s1)+1]] -=1
            if dic2[s2[j-len(s1)+1]] == 0:
                dic2.pop(s2[j-len(s1)+1])
        return False
