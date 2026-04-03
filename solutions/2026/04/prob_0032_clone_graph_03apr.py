from typing import List, Optional
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Approach: 
            - Create a dictionary to store nodes as keys and their clones as values.
            - Use DFS to traverse the graph and create clones for each node.

        Time Complexity: O(N), where N is the number of nodes in the graph.
        Space Complexity: O(N), due to the space required by the dictionary and the cloned nodes.
        """
        # Create a dictionary to store nodes as keys and their clones as values
        clone_map = defaultdict(lambda: None)

        def dfs(node):
            if not node:
                return None

            # If the node has already been cloned, return its clone
            if clone_map[node]:
                return clone_map[node]

            # Create a new node with the same value
            clone_node = Node(node.val)

            # Clone all neighbors of the current node
            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                clone_node.neighbors.append(clone_neighbor)

            # Store the cloned node in the dictionary
            clone_map[node] = clone_node

            return clone_node

        # Start DFS from the root node
        return dfs(node)