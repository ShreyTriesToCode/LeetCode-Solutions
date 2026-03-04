from typing import List, Optional

class Solution:
    def longestSubstring(self, s: str) -> int:
        """
        Approach: 
        We use a sliding window approach with a set to keep track of unique characters in the current substring.
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.
        """
        # Initialize variables
        max_length = 0
        char_set = set()
        left = 0

        # Iterate over the string
        for right in range(len(s)):
            # While the current character is in the set, remove the leftmost character
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("abcabcbb"))  # Expected: 3
    print(s.longestSubstring("bbbbb"))  # Expected: 1
    print(s.longestSubstring("pwwkew"))  # Expected: 3
    print(s.longestSubstring(""))  # Expected: 0
    print(s.longestSubstring("abcdefghijklmnopqrstuvwxyz"))  # Expected: 26