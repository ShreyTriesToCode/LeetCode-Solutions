from typing import List, Optional

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Dynamic Programming. We use a dp array where dp[i] is True if the string from index 0 to i can be segmented into words from the wordDict.
        Time Complexity: O(n*m) where n is the length of s and m is the number of words in the wordDict.
        Space Complexity: O(n) for the dp array.
        """
        # Initialize the dp array with False values
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Iterate over the string
        for i in range(1, len(s) + 1):
            # Iterate over the substring ending at i
            for j in range(i):
                # If the substring from j to i is in the wordDict and the substring from 0 to j can be segmented, then the substring from 0 to i can be segmented
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        # Return the last element of the dp array
        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected: False