class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m * n)
        Space Complexity: O(1)

        The idea is to build up a table that stores the minimum sum of each cell.
        We start from the first row and first column, and for each cell, we calculate
        the minimum sum by taking the current value and adding the minimum of the values
        in the top or left cells.

        :param grid: A 2D list representing the grid
        :return: The minimum path sum
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # Initialize the first row and column
        for i in range(m):
            dp[i][0] = grid[i][0]
        for j in range(n):
            dp[0][j] = grid[0][j]

        # Fill up the rest of the table
        for i in range(1, m):
            for j in range(1, n):
                # Calculate the minimum sum by taking the current value and adding the minimum of the values in the top or left cells
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # The minimum path sum is stored in the bottom-right cell
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Expected: 7
    print(s.minPathSum([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: 12