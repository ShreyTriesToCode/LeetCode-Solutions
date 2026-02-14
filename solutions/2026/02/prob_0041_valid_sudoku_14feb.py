from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Approach: We will use two sets to track the numbers in each row and column.
        Time Complexity: O(81), because we need to check all 81 cells.
        Space Complexity: O(1), because the size of the sets is constant.
        """

        # Create sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate over each cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                # If the number is empty, skip it
                if not num:
                    continue

                # Calculate the box index
                box_index = (i // 3) * 3 + j // 3

                # Check if the number already exists in the row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                # Add the number to the sets for its row, column, and box
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        # If we've checked all cells and haven't returned False, the board is valid
        return True