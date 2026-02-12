from typing import List, Optional

class Solution:
    def decodeWays(self, s: str) -> int:
        """
        Approach: Dynamic programming with memoization.
        Time Complexity: O(n)
        Space Complexity: O(1), excluding input string
        """
        n = len(s)
        
        # Initialize a list to store the number of ways for each prefix of the string
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # Iterate over the string from left to right
        for i in range(1, n + 1):
            # If the current character is not '0', we can always use it as a single digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # If the last two characters are both between 10 and 26, we can combine them into a two-digit number
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.decodeWays("12"))  # Expected: 2
    print(s.decodeWays("226"))  # Expected: 3