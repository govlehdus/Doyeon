"""it is obvious to iterate the list and divide it.
so how are we going to make an algorithm to divide it. 
it will have the same alphabets, so we can use alphabet.
we can make a dictionary that has 0-26 as key and value of 0-num of the alphabet
and how are we going to put it in the same list """
#This is my first thinking
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            vals = [0] * 26
            for alp in s:
                vals[ord(alp) - ord('a')] +=1
            dict[vals].append(s)
        return dict.values()
#I got error since, I can't put list value as a key in dictionary since it is unhashable.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for s in strs:
            vals = [0] * 26
            for alp in s:
                vals[ord(alp) - ord("a")] +=1
            dict[tuple(vals)].append(s)
        return dict.values()
#This is the faster way to solve it.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


