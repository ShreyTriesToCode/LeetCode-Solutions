from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Approach: We will use three sets to track the values in each row, column and 3x3 box.
        Time Complexity: O(81) because we are iterating over each cell in the board.
        Space Complexity: O(1) because we are using a constant amount of space to store the sets.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i] or val in cols[j] or val in boxes[(i//3)*3 + j//3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i//3)*3 + j//3].add(val)

        return True

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]))  # Expected: True

    print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]))  # Expected: False