from typing import List, Optional
import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach: 
        Time Complexity: O(4^n / n^(3/2))
        Space Complexity: O(n)
        
        This solution uses a backtracking approach to generate all possible combinations of parentheses.
        
        The idea is to start with an empty string and then add either an open or close parenthesis at each step.
        We use a recursive function to try both possibilities and backtrack when necessary.
        """
        def backtrack(s, left, right):
            # Base case: if the length of the string is equal to 2n
            if len(s) == 2 * n:
                result.append("".join(s))
                return
            
            # If we can add an open parenthesis, do so and recurse
            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
            
            # If we can add a close parenthesis, do so and recurse
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()

        result = []
        backtrack([], 0, 0)
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))  # Expected: ['((()))', '(()())', '(())()', '()(())', '()()()' ]