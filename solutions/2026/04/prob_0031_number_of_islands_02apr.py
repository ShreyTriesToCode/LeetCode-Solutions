from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: Depth-First Search (DFS) to mark visited cells and count islands.
        
        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns in the grid.
        Space Complexity: O(R*C), due to the recursive call stack and the visited set.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            """Mark all connected cells as visited."""
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            visited[r][c] = True

            # Mark adjacent cells as visited.
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        return count