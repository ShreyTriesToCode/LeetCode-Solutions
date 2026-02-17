from typing import List, Optional

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[Optional[int]]:
        """
        Approach: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Create a hash table to store the numbers we have seen so far and their indices.
        Iterate through the list of numbers. For each number, calculate its complement (target - number).
        If the complement is in the hash table, return the index of the complement and the current number as the solution.
        Otherwise, add the current number to the hash table.
        
        :param numbers: A sorted list of integers
        :type numbers: List[int]
        :param target: The target sum
        :type target: int
        :return: A list containing the indices of the two numbers that add up to the target
        :rtype: List[Optional[int]]
        """
        # Create a hash table to store the numbers we have seen so far and their indices
        num_dict = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(numbers):
            # Calculate its complement (target - number)
            complement = target - num
            
            # If the complement is in the hash table, return the index of the complement and the current number as the solution
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number to the hash table
            num_dict[num] = i
        
        # If no solution is found, return an empty list
        return []