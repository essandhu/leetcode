class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        totalRows, totalCols = len(boxGrid), len(boxGrid[0])
        rotated = [["."] * totalRows for _ in range(totalCols)]

        for row in range(totalRows):
            bottom = totalCols - 1

            for col in reversed(range(totalCols)):
                if boxGrid[row][col] == "#":
                    rotated[bottom][totalRows - row - 1] = "#"
                    bottom -= 1
                elif boxGrid[row][col] == "*":
                    rotated[col][totalRows - row - 1] = "*"
                    bottom = col - 1

        return rotated