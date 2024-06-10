class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        val = sum(arr[:k])
        for i in range(len(arr)-k+1):
            if val / k >= threshold:
                res +=1
            if i + k < len(arr):
                val -= arr[i]
                val += arr[i+k]
        return res
