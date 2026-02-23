from typing import List, Optional
from collections import deque

class Solution:
    def maxSlidingMap(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: We use a deque to store the indices of the elements in the current window.
        We also maintain a max heap to store the maximum element in the current window.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialize the result list and the deque
        result = []
        dq = deque()

        # Iterate over the input list
        for i, num in enumerate(nums):
            # Remove the indices of the elements that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove the indices of the elements that are smaller than the current element
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # Add the index of the current element to the deque
            dq.append(i)

            # If the window is full, add the maximum element to the result list
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingMap([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3, 3, 5, 5, 6, 7]
    print(s.maxSlidingMap([1, 2, 3, 4, 5], 3))  # Expected: [3, 4, 5]
    print(s.maxSlidingMap([1, 2, 3, 4, 5], 1))  # Expected: [1]