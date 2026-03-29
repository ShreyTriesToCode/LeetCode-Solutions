def houseRobber(nums: List[int]) -> int:
    def helper(i, j):
        if i >= len(nums) or j >= len(nums):
            return 0
        if i == j:
            return nums[i]
        if dp[i][j] != -1:
            return dp[i][j]
        
        res = max(helper(i+2, j), helper(i+1, j-1) + nums[j])
        dp[i][j] = res
        return res
    
    n = len(nums)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    res = helper(0, n-1)
    return res

# --- Test Cases ---
if __name__ == '__main__':
    nums = [1,2,3,1]
    print(houseRobber(nums))  # Expected: 4
    nums = [2,7,9,3,1]
    print(houseRobber(nums))  # Expected: 12