from typing import List, Optional

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        The idea is to create a dp array where dp[i] represents the number of ways 
        we can reach the ith stair. We initialize dp[0] and dp[1] as 1 since there's 
        only one way to reach the first stair (by not moving) and two ways to reach 
        the second stair (by taking one step or by skipping one step).
        
        Then, for each i from 2 to n, we calculate dp[i] as the sum of dp[i-1] and 
        dp[i-2]. This is because we can either take one step from the previous stair 
        or skip one step and move two steps at a time.
        """
        if n <= 2:
            return n
        
        # Initialize dp array with zeros
        dp = [0]*(n+1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill up the dp array
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))  # Expected: 3
    print(s.climbStairs(5))  # Expected: 5