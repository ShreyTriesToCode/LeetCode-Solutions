def climbStairs(self, steps: int) -> int:
    dp = [0] * (steps + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, steps + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[-1]