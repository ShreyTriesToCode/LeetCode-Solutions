from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize output array with all elements as 1
        output = [1] * n
        
        # Calculate the prefix products
        left_prefix_product = 1
        for i in range(n):
            output[i] *= left_prefix_product
            left_prefix_product *= nums[i]
        
        # Calculate the suffix products and multiply with prefix products
        right_suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_suffix_product
            right_suffix_product *= nums[i]
        
        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # Expected: [24, 12, 8, 6]
    print(s.productExceptSelf([1, 1, 1, 1]))  # Expected: [1, 1, 1, 1]
    print(s.productExceptSelf([2, 3, -2, -4]))  # Expected: [-8, 12, -6, 8]