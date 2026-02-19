from typing import List, Optional

class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We create two arrays dp1 and dp2 where dp1[i] represents the maximum amount of money we can get if we rob up to the i-th house in the first half of the array and dp2[i] represents the maximum amount of money we can get if we rob up to the i-th house in the second half of the array.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # If there are no houses, return 0
        if not nums:
            return 0
        
        # Initialize dp1 and dp2 for the first house
        dp1 = [nums[0]]
        dp2 = [0]
        
        # Iterate over the rest of the houses
        for i in range(1, len(nums)):
            # For each house, we have two options: rob it or not rob it
            # If we rob it, we add the amount to dp1[i-1] but subtract the amount from dp2[i-1]
            # If we don't rob it, we just take the maximum of dp1[i-1] and dp2[i-1]
            new_dp1 = max(dp1[i-1], dp2[i-1]) + nums[i]
            new_dp2 = max(dp1[i-1], dp2[i-1])
            
            # Update dp1 and dp2
            dp1.append(new_dp1)
            dp2.append(new_dp2)
        
        # The maximum amount of money we can get is the maximum of dp1[-1] and dp2[-1]
        return max(dp1[-1], dp2[-1])

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.houseRobber([1, 2, 3, 1]))  # Expected: 4
    print(s.houseRobber([2, 7, 9, 3, 1]))  # Expected: 12