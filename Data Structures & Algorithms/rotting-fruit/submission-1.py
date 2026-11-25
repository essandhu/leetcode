class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        freshCount = 0
        time = 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshCount += 1
                    
                if grid[row][col] == 2:
                    queue.append((row, col))

        while freshCount > 0 and queue:
            length = len(queue)

            for index in range(length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    tempRow, tempCol = row + dr, col + dc
                    
                    if (tempRow in range(len(grid)) and tempCol in range(len(grid[0])) and grid[tempRow][tempCol] == 1):
                        grid[tempRow][tempCol] = 2
                        queue.append((tempRow, tempCol))
                        freshCount -= 1

            time += 1

        return time if freshCount == 0 else -1