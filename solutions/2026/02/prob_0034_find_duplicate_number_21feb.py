def findDuplicate(nums: List[int]) -> int:
    """
    Approach: Floyd's Tortoise and Hare (Cycle Detection) algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Reset hare to start of list
    hare = nums[0]
    # Move both tortoise and hare one step at a time
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

# --- Test Cases ---
if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(findDuplicate(nums))  # Expected: 2

    nums = [3, 1, 3, 4, 2]
    print(findDuplicate(nums))  # Expected: 3

    nums = [1, 1, 2]
    print(findDuplicate(nums))  # Expected: 1