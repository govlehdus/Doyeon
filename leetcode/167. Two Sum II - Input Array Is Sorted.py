#First I try to iterate it one time with one constant memory. I choose to make a dictionary to store the index and value.
#While iterating through the list, I check the target-value is in the dictionary or not, and if it it there, return the indexes.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, value in enumerate(numbers):
            key = target - value
            if key in dic:
                return [dic[key]+1 , i+1]
            else:
                dic[value] = i
