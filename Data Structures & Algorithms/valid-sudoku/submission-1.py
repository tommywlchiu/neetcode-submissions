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

                sqr_key = (row // 3, col // 3)   
                if val in rows[row] or val in cols[col] or val in sqrs[sqr_key]:
                    return False

                rows[row].add(val)
                cols[col].add(val) 
                sqrs[sqr_key].add(val) 
                
        return True