from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: 
            We use a breadth-first search (BFS) approach to traverse the binary tree level by level.
            We use a queue data structure to keep track of nodes at each level.

        Time Complexity: O(N), where N is the number of nodes in the tree.
        Space Complexity: O(W), where W is the maximum width of the tree.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            # Get the size of the current level
            level_size = len(queue)

            # Initialize a list to store the nodes at the current level
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()

                # Add the node's value to the list of nodes at the current level
                level_nodes.append(node.val)

                # If the node has children, add them to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the list of nodes at the current level to the result
            result.append(level_nodes)

        return result