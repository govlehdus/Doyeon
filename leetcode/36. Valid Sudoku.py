"""To find a valid sudoku, I will first create 3 sets of rows, columns, and boxes.
Using nested for loop, to iterate all numbers, and put into the sets. Check whether
the value is already exists in the set or not, if it is, return False."""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if (board[i][j] in column[i] or
                    board[i][j] in rows[j] or
                    board[i][j] in boxes[(i // 3, j // 3)]):
                        return False
                    else:
                        column[i].add(board[i][j])
                        rows[j].add(board[i][j])
                        boxes[(i // 3, j // 3)].add(board[i][j])
        return True
