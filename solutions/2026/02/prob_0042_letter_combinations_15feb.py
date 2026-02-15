from typing import List, Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Approach: Backtracking with string manipulation
        Time Complexity: O(4^n), where n is the number of digits
        Space Complexity: O(n), where n is the number of possible combinations
        """
        
        # Define a list of possible letters for each digit
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        # Base case: if digits is empty, return an empty list
        if not digits:
            return []
        
        # Recursive function to generate combinations
        def backtrack(combination, next_digits):
            # If there are no more digits to process, add the current combination to the result
            if len(next_digits) == 0:
                output.append(combination)
            else:
                # For each possible letter for the current digit
                for letter in phone[next_digits[0]]:
                    # Recursively call backtrack with the updated combination and next_digits
                    backtrack(combination + letter, next_digits[1:])
        
        # Initialize an empty list to store the result
        output = []
        
        # Call the recursive function with an empty string as the initial combination and digits as the input
        backtrack("", digits)
        
        # Return the result
        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))  # Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']