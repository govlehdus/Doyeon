class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        val1 = len(nums1)
        val2 = len(nums2)
        newnum = []
        l, r = 0,0
        while l < val1 and r < val2:
            if nums1[l] < nums2[r]:
                newnum.append(nums1[l])
                l +=1
            else:
                newnum.append(nums2[r])
                r +=1
        if l < val1:
            newnum = newnum + nums1[l:]
        if r < val2:
            newnum = newnum + nums2[r:]
        if (val1 + val2) % 2 == 1:
            return newnum[(val1+val2)//2]
        else:
            return (newnum[(val1+val2)//2] + newnum[((val1+val2)//2)-1] ) /2 
