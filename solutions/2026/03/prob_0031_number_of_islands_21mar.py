from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: 
        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns in the grid.
        Space Complexity: O(1), as we are not using any additional space that scales with input size.

        The idea is to perform a depth-first search (DFS) on each land cell. 
        When DFS reaches an ocean cell, it marks all adjacent cells as visited by setting them to '0'. 
        This way, the number of islands can be counted by counting the number of land cells left after DFS.
        """
        
        # Check if grid is empty
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Check if cell is within bounds and is a land cell
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited by setting it to '0'
            grid[r][c] = '0'

            # Recursively call DFS on adjacent cells
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                # If the current cell is a land cell, increment the count and perform DFS
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        
        return count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 1
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 1
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","0","0","0"],["0","0","0","1","1"]]))  # Expected: 2