class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        spiral = []

        rows, cols = len(matrix), len(matrix[0])
        curRow, curCol = 0, 0
        directionIndex = 0
        visited = set()

        for index in range(rows * cols):
            spiral.append(matrix[curRow][curCol])
            visited.add((curRow, curCol))

            nextRow = curRow + directions[directionIndex][0]
            nextCol = curCol + directions[directionIndex][1]

            if not (0 <= nextRow < rows and 0 <= nextCol < cols and (nextRow, nextCol) not in visited):
                directionIndex = (directionIndex + 1) % 4
            
            curRow += directions[directionIndex][0]
            curCol += directions[directionIndex][1]
        
        return spiral