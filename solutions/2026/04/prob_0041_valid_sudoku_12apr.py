from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Approach: We will use two sets to keep track of the numbers in each row and column.
        Time Complexity: O(81) because we are iterating over all cells in the Sudoku board
        Space Complexity: O(1) because we are using a constant amount of space to store our sets
        """
        
        # Create sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate over each cell in the board
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # If the value is not empty
                if val != '.':
                    
                    # Calculate the box index
                    box_index = (i // 3) * 3 + j // 3
                    
                    # Check if the number already exists in the row, column, or box
                    if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                        return False
                    
                    # Add the number to the sets for its row, column, and box
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box_index].add(val)

        # If we have checked all cells and haven't returned False, then the board is valid
        return True

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]))  # Expected: True

    print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]))  # Expected: False