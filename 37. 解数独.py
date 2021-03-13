class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def dfs(index=0):
            if index >= len(could_place):
                return True
            row, col = could_place[index]
            for d in rows[row] & cols[col] & boxes[box_index(row, col)]:
                rows[row].remove(d)
                cols[col].remove(d)
                boxes[box_index(row, col)].remove(d)
                board[row][col] = d
                if dfs(index + 1):
                    return True
                rows[row].add(d)
                cols[col].add(d)
                boxes[box_index(row, col)].add(d)
            return False

        def box_index(row, col):
            return (row // 3) * 3 + col // 3

        rows = [set(str(i) for i in range(1, 10)) for i in range(9)]
        cols = [set(str(i) for i in range(1, 10)) for i in range(9)]
        boxes = [set(str(i) for i in range(1, 10)) for i in range(9)]
        could_place = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    boxes[box_index(i, j)].remove(board[i][j])
                else:
                    could_place.append((i, j))
        self.one_to_nine = set(str(i) for i in range(1, 10))
        self.sudoku_solved = False
        dfs()


sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
s.solveSudoku(sudoku)
print(sudoku)
