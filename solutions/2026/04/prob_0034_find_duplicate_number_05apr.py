def findDuplicate(nums: List[int]) -> int:
    """
    Approach: Floyd's Tortoise and Hare algorithm, also known as the "cycle detection" algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Phase 1: Detecting the cycle
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Finding the start of the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare