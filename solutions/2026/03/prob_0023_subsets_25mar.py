from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: 
        Time Complexity: O(2^n)
        Space Complexity: O(2^n)

        This problem is a classic example of a backtracking problem. We can use recursion to generate all possible subsets.
        The idea is to start with an empty subset and then for each number in the input list, we add it to the current subset
        and recursively generate all subsets of the remaining numbers.

        :param nums: A list of integers
        :return: A list of lists, where each sublist is a subset of the input list
        """
        # Base case: if the input list is empty, return an empty list
        if not nums:
            return []

        # Recursive case: get all subsets of the remaining numbers
        result = self.subsets(nums[1:])
        
        # For each number in the input list, add it to each subset of the remaining numbers
        for i in range(len(result)):
            result[i] = [nums[0]] + result[i]
        
        # Add an empty subset at the beginning of the result
        result.insert(0, [])
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[], [0]]