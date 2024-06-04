class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        startIndex = 0
        pmap, smap = {},{}
        res = []
        
        for char in p:
            pmap[char] = 1 + pmap.get(char,0)
        
        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i],0)
            
            if i >= len(p) -1:
                if smap == pmap:
                    res.append(startIndex)
                smap[s[startIndex]] -=1
                if smap[s[startIndex]] == 0:
                    del smap[s[startIndex]]
                startIndex +=1
        return res
