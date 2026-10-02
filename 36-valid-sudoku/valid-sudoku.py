
class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                x = board[r][c]

                if x == ".":
                    continue

                b = (r // 3) * 3 + c // 3

                if x in rows[r] or x in cols[c] or x in boxes[b]:
                    return False

                rows[r].add(x)
                cols[c].add(x)
                boxes[b].add(x)

        return True