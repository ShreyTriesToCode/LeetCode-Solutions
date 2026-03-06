from typing import List, Optional

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: 
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # odd length palindrome
            odd_palindrome = expandAroundCenter(i, i)
            # even length palindrome
            even_palindrome = expandAroundCenter(i, i + 1)
            longest = max([longest, odd_palindrome, even_palindrome], key=len)

        return longest

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))  # Expected: "bab"
    print(s.longestPalindrome("cbbd"))  # Expected: "bb"