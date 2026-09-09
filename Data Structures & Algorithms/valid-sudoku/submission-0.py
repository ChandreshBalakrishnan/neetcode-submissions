class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                box = (r//3) * 3 + (c//3)

                if num in rows[r] or num in col[c] or num in sq[box]:
                    return False
                rows[r].add(num)
                col[c].add(num)
                sq[box].add(num)
        
        return True
                