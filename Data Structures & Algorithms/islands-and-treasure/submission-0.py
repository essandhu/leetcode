class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def addCell(row, col):
            if (min(row, col) < 0 or row == rows or col == cols or (row, col) in visited or grid[row][col] == -1):
                return

            visited.add((row, col))
            queue.append([row, col])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))


        dist = 0

        while queue:
            for index in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)

            dist += 1
        