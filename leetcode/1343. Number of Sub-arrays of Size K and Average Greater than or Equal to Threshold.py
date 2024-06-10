class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        val = sum(arr[:k-1])
        for i in range(len(arr)-k+1):
            val += arr[i+k-1]
            if val / k >= threshold:
                res +=1
           
            val -= arr[i]
            
        return res
