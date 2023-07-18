#I will make a set of nums and check the length of the set and list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        return len(dup) != len(nums)
#This has better efficiency since instead of making a full set, it adds one by one and return True if one element is already inside the set.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
