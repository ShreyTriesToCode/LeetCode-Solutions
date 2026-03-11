from typing import List

class Solution:
    def decodeWays(self, s: str) -> int:
        """
        This function calculates the number of ways to decode a given string.
        A string can be decoded in multiple ways if it contains two or more consecutive digits that range from 10 to 26.
        For example, "12" can be decoded as "AB" or "L", "23" can be decoded as "XY" or "W", etc.
        """
        n = len(s)
        # Initialize a list to store the number of ways to decode the string up to each position
        dp = [0] * (n + 1)
        dp[0] = 1  # There is one way to decode an empty string
        dp[1] = 1  # There is one way to decode a single digit

        # Iterate over the string from the second digit to the end
        for i in range(2, n + 1):
            # If the current digit is not 0, we can decode it separately
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # If the last two digits are between 10 and 26, we can decode them together
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        # The number of ways to decode the entire string is stored in the last position of the list
        return dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.decodeWays("12"))  # Expected: 2
    print(s.decodeWays("226"))  # Expected: 3
    print(s.decodeWays("0"))  # Expected: 0
    print(s.decodeWays("10"))  # Expected: 1