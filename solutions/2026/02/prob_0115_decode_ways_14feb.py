from typing import List, Optional

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Approach: 
        This problem can be solved using dynamic programming. We will create two arrays, one for the number of ways to decode a string ending at each position and another for the actual strings that can be decoded.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Base case
        if not s:
            return 0
        
        # Initialize variables
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # If the current character is not zero, we can decode it separately
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # If the last two characters form a number between 10 and 26, we can decode them together
            if '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    # Test 1
    print(s.numDecodings("226"))  # Expected: 3
    # Test 2
    print(s.numDecodings("00"))  # Expected: 0