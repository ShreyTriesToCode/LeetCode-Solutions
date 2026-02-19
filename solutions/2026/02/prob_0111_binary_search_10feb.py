from typing import List, Optional

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        """
        Approach: This problem can be solved using a modified version of the standard binary search algorithm.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Initialize two pointers, one at the start and one at the end of the list
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            # If the target is less than the middle element, move the right pointer
            elif nums[mid] > target:
                right = mid - 1
            # If the target is greater than the middle element, move the left pointer
            else:
                left = mid + 1
        
        # If the target is not found, return -1
        return -1

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.binarySearch([1, 3], 0))  # Expected: -1
    print(s.binarySearch([1, 3], 2))  # Expected: 1
    print(s.binarySearch([1, 3], 4))  # Expected: -1