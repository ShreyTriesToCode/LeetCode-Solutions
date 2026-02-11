from typing import List, Optional

class Solution:
    def minimumTotal(self, nums: List[int]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m)
        Space Complexity: O(m)
        """
        m = len(nums)
        dp = [[0] * (m + 1) for _ in range(m)]
        
        # Initialize the first row of dp
        for j in range(m):
            dp[0][j] = nums[j]
            
        # Fill up the rest of dp
        for i in range(1, m):
            for j in range(m):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + nums[i]
                elif j == m - 1:
                    dp[i][j] = dp[i-1][j-1] + nums[i]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + nums[i]
                    
        # Return the minimum path sum
        return min(dp[m - 1])

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([1,3,1]))  # Expected: 2
    print(s.minimumTotal([1,3,1,4,1,4,6,7,8,9,2,5,0,3,4]))  # Expected: 11