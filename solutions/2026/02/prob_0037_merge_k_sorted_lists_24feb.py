from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: We will use a min heap to keep track of the smallest node from each list.
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists.
        Space Complexity: O(k) for the heap.
        """
        # Create a min heap to store the smallest node from each list
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                # Push the node's value, list index, and node into the heap
                heapq.heappush(min_heap, (node.val, i, node))

        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy

        # While the heap is not empty
        while min_heap:
            # Get the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            # If there are more nodes in the list, push the next node into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # Return the merged list
        return dummy.next