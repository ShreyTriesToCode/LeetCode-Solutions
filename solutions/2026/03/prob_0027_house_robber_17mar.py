from typing import List, Optional

class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming. 
                  We create two arrays, dp1 and dp2, where dp1[i] represents the maximum amount of money we can get if we rob up to the i-th house starting from the first house, and dp2[i] represents the maximum amount of money we can get if we rob up to the i-th house starting from the second house.
                  We then return the maximum value between dp1[-1] and dp2[-1], because either way we will always have one less house to rob.

        Time Complexity: O(n), where n is the number of houses. 
        Space Complexity: O(n), where n is the number of houses.
        """
        # Base case
        if not nums:
            return 0

        # Initialize dp1 and dp2 with the first element of nums
        dp1 = [nums[0]]
        dp2 = [0]

        # Fill up dp1 and dp2
        for i in range(1, len(nums)):
            dp1.append(max(dp1[i-1], dp2[i-1] + nums[i]))
            dp2.append(max(dp1[i-1], dp2[i-1]) + nums[i])

        # Return the maximum value between dp1[-1] and dp2[-1]
        return max(dp1[-1], dp2[-1])

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.houseRobber([1, 2, 3, 1]))  # Expected: 4
    print(s.houseRobber([2,7,9,3,1]))  # Expected: 12