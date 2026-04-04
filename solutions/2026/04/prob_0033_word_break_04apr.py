class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        The idea is to build a boolean array dp where dp[i] represents whether the string from index 0 to i can be segmented into words in the wordDict.
        We start by initializing all values of dp as False except for dp[0], which is True because an empty string can always be segmented.
        Then we iterate over the string and for each character, we check if it's in the wordDict. If it's not, then we cannot segment this string into words from the wordDict. 
        If it is, then we check all substrings ending at this character to see if they can be segmented into words from the wordDict.
        
        :param s: The input string
        :type s: str
        :param wordDict: A list of words that can be used for segmentation
        :type wordDict: List[str]
        :return: Whether the string can be segmented into words in the wordDict
        :rtype: bool
        """
        
        # Initialize a boolean array dp with size len(s) + 1, all values are initially False except for dp[0] which is True.
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        # Iterate over the string from index 1 to the end
        for i in range(1, len(s) + 1):
            # For each character, check if it's in the wordDict
            for j in range(i):
                # If the substring from index j to i is in the wordDict and the substring from index 0 to j can be segmented into words from the wordDict, then the string from index 0 to i can also be segmented.
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        # Return whether the string can be segmented into words from the wordDict
        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected: False