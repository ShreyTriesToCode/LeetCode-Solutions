from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> ListNode:
        """
        Approach: We use a min-heap to store nodes from all lists. The heap is sorted by node value.
        Time Complexity: O(N log k), where N is the total number of nodes and k is the number of lists.
        Space Complexity: O(k), for storing the heap.
        """
        # Create a min-heap
        min_heap = []
        
        # Add the first node from each list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Initialize the dummy head and current tail of the result list
        dummy_head = ListNode(0)
        current_tail = dummy_head
        
        # While the heap is not empty
        while min_heap:
            # Get the smallest value from the heap
            val, list_index, node = heapq.heappop(min_heap)
            
            # Add the node to the result list
            current_tail.next = node
            current_tail = current_tail.next
            
            # If there are more nodes in the list, add the next one to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))
        
        # Return the result list (excluding the dummy head)
        return dummy_head.next