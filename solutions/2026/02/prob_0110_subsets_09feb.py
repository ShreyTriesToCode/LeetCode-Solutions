from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking with recursion to generate all possible subsets.
        Time Complexity: O(2^n) where n is the number of elements in the input list
        Space Complexity: O(n) for storing the current subset and recursive call stack
        """
        # Initialize an empty list to store the result
        result = []
        
        # Define a helper function for recursion
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            
            # Iterate over the remaining elements in the input list
            for i in range(start, len(nums)):
                # Recursively call the backtrack function with the next element
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack by removing the last added element from the subset
                path.pop()
        
        # Start the backtracking process from the first element
        backtrack(0, [])
        
        # Return the result
        return result

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # [[]]