class Solution:
    def decodeWays(self, s: str) -> int:
        """
        Approach: This problem can be solved using dynamic programming. We will create a table to store the number of ways to decode the string up to each position.
        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), where n is the length of the string.
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # If the current character is not 0, we can decode it separately
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # If the last two characters are between 10 and 26, we can decode them together
            if i >= 2 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]