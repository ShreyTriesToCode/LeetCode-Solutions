from typing import List, Optional

class Solution:
    def longestIncreasingSubsequence(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We initialize a list dp where dp[i] will store the length of the longest increasing subsequence ending at index i.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.longestIncreasingSubsequence([10,9,2,5,3,7,101,18])) # Expected: 4
    print(s.longestIncreasingSubsequence([0,1,0,3,2,3])) # Expected: 4