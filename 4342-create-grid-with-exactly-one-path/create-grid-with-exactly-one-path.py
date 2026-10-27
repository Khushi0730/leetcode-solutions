from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [['#'] * n for _ in range(m)]
        i = j = 0
        grid[0][0] = '.'
        step_right = True
        while (i, j) != (m - 1, n - 1):
            if step_right and j + 1 < n:
                j += 1
            elif not step_right and i + 1 < m:
                i += 1
            elif j + 1 < n:
                j += 1
            else:
                i += 1
            grid[i][j] = '.'
            step_right = not step_right
        return [''.join(row) for row in grid]