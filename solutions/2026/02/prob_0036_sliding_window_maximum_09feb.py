from typing import List, Optional
import heapq

class Solution:
    def maxSlidingMap(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: We use a deque to store indices of elements in descending order.
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        # Initialize the result list and the deque
        result = []
        dq = []

        # Iterate over the input list
        for i, num in enumerate(nums):
            # Remove indices of elements that are out of the current window
            while dq and dq[0] <= i - k:
                heapq.heappop(dq)

            # Add the index of the current element to the deque
            if not dq or nums[dq[-1]] < num:
                heapq.heappush(dq, i)

            # If the current element is within the window, add it to the result list
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingMap([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(s.maxSlidingMap([1], 1))  # Expected: [1]