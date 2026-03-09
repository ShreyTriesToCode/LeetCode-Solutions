from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: We use a min heap to keep track of the smallest element from each list.
        Time Complexity: O(N log k) where N is the total number of elements and k is the number of lists.
        Space Complexity: O(k) for the heap.
        """
        # Create a min heap and push the first element from each list into the heap
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Create a dummy node to serve as the head of the result list
        dummy = ListNode(0)
        current = dummy
        
        # While the heap is not empty, pop the smallest element and add it to the result list
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If there are more elements in the list, push the next element into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        # Return the head of the result list
        return dummy.next