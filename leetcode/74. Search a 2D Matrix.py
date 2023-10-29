#Using two binary search, find the which row is the right row first, and then find the position of the target.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        column = len(matrix)
        bottom, top = 0, column -1
        while top >= bottom:
            mid = bottom + (top- bottom)//2
            if target > matrix[mid][row-1]:
                bottom = mid+1
            elif target < matrix[mid][0]:
                top = mid -1
            else:
                break
        
        l,r = 0, row-1

        while r >= l:
            m = l + (r-l)//2
            if matrix[mid][m] > target:
                r = m -1
            elif matrix[mid][m] < target:
                l = m +1
            else:
                return True
        return False
