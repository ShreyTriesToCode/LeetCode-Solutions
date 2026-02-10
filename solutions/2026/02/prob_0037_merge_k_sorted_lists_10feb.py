from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: We use a min heap to keep track of the smallest node in each list.
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists.
        Space Complexity: O(k)
        """
        
        # Create a min heap and add the first node from each list
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Initialize the dummy head of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        
        while min_heap:
            # Get the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)
            
            # Add the node to the result list
            current.next = node
            current = current.next
            
            # If there are more nodes in the list, add the next one to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy_head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next