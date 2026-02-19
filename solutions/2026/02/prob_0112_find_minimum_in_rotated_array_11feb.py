from typing import List, Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved by using a modified binary search algorithm.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Step 1: Find the first occurrence of the minimum element
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # Step 2: Verify that the found element is indeed the minimum
        return nums[left]

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([4,5,6,7,0,1,2]))  # Expected: 0
    print(s.findMin([3,4,5,1,2]))  # Expected: 1