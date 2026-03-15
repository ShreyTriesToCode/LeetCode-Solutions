from typing import List, Optional

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        The idea is to create a 2D array where each cell represents the number of ways to reach that point from the top-left corner.
        We start by initializing all cells on the first row and first column to 1, since there's only one way to reach any point in these rows and columns (by always moving right or down respectively).
        Then we fill in the rest of the array based on the number of ways to reach the cell above it and the cell to its left.
        Finally, we return the value at the bottom-right corner of the array, which represents the total number of unique paths from the top-left corner to the bottom-right corner.

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Initialize a 2D array with zeros
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize all cells on the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the rest of the array based on the number of ways to reach each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Return the value at the bottom-right corner of the array
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(10, 20))  # Expected: 184756