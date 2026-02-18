from typing import List, Optional

class Solution:
    def longestSubstringWithoutRepeatingCharacters(self, s: str) -> int:
        """
        Approach: This problem can be solved using a sliding window approach with a set to keep track of unique characters.
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.
        """
        # Initialize variables
        left = 0
        max_length = 0
        char_set = set()

        # Iterate over the string
        for right in range(len(s)):
            # While the current character is in the set, remove the leftmost character from the set and move the window to the right
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length