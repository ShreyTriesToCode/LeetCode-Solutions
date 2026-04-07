from typing import List, Optional
from collections import deque

class Solution:
    def maxSlidingArray(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: We use a double-ended queue to store indices of elements in the current window.
        The queue is ordered such that the front always contains the maximum element seen so far.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        # Initialize an empty deque to store indices
        dq = deque()
        
        # Initialize the result list
        res = []
        
        # Iterate over the input array
        for i, num in enumerate(nums):
            # Remove elements from the back of the queue that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove elements from the front of the queue that are smaller than the current element
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            # Add the current index to the back of the queue
            dq.append(i)
            
            # If the window is full, add the maximum element to the result list
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingArray([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(s.maxSlidingArray([1], 1))  # Expected: [1]