from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: This problem can be solved using bit manipulation and recursion.
        Time Complexity: O(2^n), where n is the number of elements in the input list.
        Space Complexity: O(2^n), as we need to store all possible subsets in our result list.
        """
        # Initialize an empty list to store the result
        result = []
        
        # Calculate the total number of subsets (2^n)
        num_subsets = 1 << len(nums)
        
        # Iterate over each subset
        for i in range(num_subsets):
            # Initialize an empty list to store the current subset
            subset = []
            
            # Convert the current subset index to binary and iterate over each bit
            for j in range(len(nums)):
                # If the jth bit is set, add the jth element of nums to the current subset
                if (i >> j) & 1:
                    subset.append(nums[j])
            
            # Add the current subset to the result list
            result.append(subset)
        
        # Return the result list
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[], [0]]