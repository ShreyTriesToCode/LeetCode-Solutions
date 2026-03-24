from typing import List, Optional

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: 
            We will use a depth-first search (DFS) algorithm to traverse the board.
            The DFS will be performed in all eight directions (up, down, left, right, and four diagonals).
            If we find the first character of the word in any direction, we will continue the DFS
            until we either find the entire word or reach a dead end.

        Time Complexity: O(N*M*4^L), where N is the number of rows, M is the number of columns,
            L is the length of the word. This is because in the worst case scenario, we need to
            traverse each cell in the board once and perform DFS for each character in the word.

        Space Complexity: O(N*M + L), where N is the number of rows, M is the number of columns,
            and L is the length of the word. This is because we need to store the current position
            in the board and the current path.
        """
        # Define all possible directions (up, down, left, right, and four diagonals)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def dfs(i: int, j: int, k: int) -> bool:
            """
            Perform DFS from the current position.
            """
            # If we have found all characters of the word, return True
            if k == len(word):
                return True

            # Check if the current position is within the board and contains a character that matches the next character in the word
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]:
                # Mark the current position as visited by changing its value to a special character
                temp = board[i][j]
                board[i][j] = '#'

                # Perform DFS in all eight directions
                for direction in directions:
                    if dfs(i + direction[0], j + direction[1], k + 1):
                        return True

                # If we have not found the next character, unmark the current position and backtrack
                board[i][j] = temp

            # If the current position does not contain a character that matches the next character in the word, return False
            return False

        # Perform DFS from each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        # If we have not found the entire word, return False
        return False