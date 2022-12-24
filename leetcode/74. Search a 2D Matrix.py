class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        while l<=r:
            m = (l+r)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif matrix[m][0] > target:
                r = m -1
            else:
                l = m +1

        l,r = 0, len(matrix[m])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                r = mid-1
            else:
                l = mid+1

        return False
