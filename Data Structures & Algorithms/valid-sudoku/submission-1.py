class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                currentVal = board[row][col]

                if currentVal == ".":
                    continue

                if currentVal in rows[row] or currentVal in cols[col] or currentVal in squares[(row // 3, col // 3)]:
                    return False
                
                rows[row].add(currentVal)
                cols[col].add(currentVal)
                squares[(row // 3, col //3)].add(currentVal)

        return True
