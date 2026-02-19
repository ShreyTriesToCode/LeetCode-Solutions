from typing import List, Optional
import heapq

class Solution:
    def medianFinder(self, nums1: List[int], nums2: List[int]) -> Optional[float]:
        """
        Approach: We use two heaps to keep track of the smaller half of each array.
        Time Complexity: O(log(m+n))
        Space Complexity: O(1)
        """
        # Create a min heap for the first array and a max heap for the second array
        min_heap = []
        max_heap = []

        # Add elements from both arrays to their respective heaps
        for num in nums1:
            heapq.heappush(min_heap, -num)  # Use negative values to simulate a max heap

        for num in nums2:
            heapq.heappush(max_heap, num)

        # Balance the heaps to ensure the size difference is at most 1
        while len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        while len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # Calculate the median
        if len(min_heap) == len(max_heap):
            return (-min_heap[0] + max_heap[0]) / 2
        else:
            return -min_heap[0]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.medianFinder([1, 3], [2]))  # Expected: 2.0
    print(s.medianFinder([1, 2], [3, 4]))  # Expected: 2.5
    print(s.medianFinder([1, 3, 5], [2, 4]))  # Expected: 3