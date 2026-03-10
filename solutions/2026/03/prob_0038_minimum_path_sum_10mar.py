from typing import List

class Solution:
    def minimumPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first element
        dp[0][0] = grid[0][0]
        
        # Fill the first row
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minimumPathSum(grid))  # Expected: 7
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minimumPathSum(grid))  # Expected: 7