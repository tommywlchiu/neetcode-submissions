class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == '.':
                    continue

                sqrs_key = (row // 3,col // 3)
                if val in rows[row] or val in cols[col] or val in sqrs[sqrs_key]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                sqrs[sqrs_key].add(val)

        return True