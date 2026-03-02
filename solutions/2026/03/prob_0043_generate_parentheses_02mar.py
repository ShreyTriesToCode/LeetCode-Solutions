from typing import List, Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach: 
        Time Complexity: O(4^n / n^(3/2))
        Space Complexity: O(4^n / n^(3/2))
        """
        def backtrack(open_paren, close_paren, path):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if open_paren < n:
                path.append("(")
                backtrack(open_paren + 1, close_paren, path)
                path.pop()
            if close_paren < open_paren:
                path.append(")")
                backtrack(open_paren, close_paren + 1, path)
                path.pop()

        result = []
        backtrack(0, 0, [])
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))  # Expected: ['((()))', '(()())', '(())()', '()(())', '()()()']