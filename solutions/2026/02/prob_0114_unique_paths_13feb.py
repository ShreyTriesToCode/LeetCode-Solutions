from typing import List, Optional

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming. 
                  We create a 2D array to store the number of unique paths 
                  from each cell to the destination.
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Create a 2D array with all elements as 0
        dp = [[0]*n for _ in range(m)]
        
        # There is only one way to reach any cell in the first row and 
        # first column, which is by always moving right or always moving down.
        dp[0][0] = 1
        for i in range(1):
            dp[i][0] = 1
            dp[0][i] = 1
        
        # Fill up the rest of the array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths is stored in the bottom right cell
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(10, 20))  # Expected: 1679616