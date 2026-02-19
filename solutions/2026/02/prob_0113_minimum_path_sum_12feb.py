from typing import List, Optional

class Solution:
    def minimumTotal(self, nums: List[int]) -> int:
        """
        Approach: Dynamic programming to build up a table of minimum sums.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Step by step implementation with comments
        n = len(nums)
        
        # Initialize the first row of the dp table
        dp = [0] * n
        dp[0] = nums[0]
        
        # Fill in the rest of the dp table
        for i in range(1, n):
            # For each cell, choose the minimum sum from the two cells above it
            dp[i] = min(dp[i-1] + nums[i], dp[i-1])
        
        # The final answer is stored in the last cell of the dp table
        return dp[-1]

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    # Test 1
    print(s.minimumTotal([1,3,1]))  # Expected: 2
    # Test 2
    print(s.minimumTotal([1,5,1,5,1]))  # Expected: 4