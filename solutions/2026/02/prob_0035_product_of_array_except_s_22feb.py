from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # left product
        left_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]

        # right product
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # Expected: [24, 12, 8, 6]
    print(s.productExceptSelf([1, 1, 1, 1]))  # Expected: [1, 1, 1, 1]
    print(s.productExceptSelf([2, 3, 4, 5]))  # Expected: [60, 40, 30, 24]