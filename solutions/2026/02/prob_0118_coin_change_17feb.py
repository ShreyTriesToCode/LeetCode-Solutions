from typing import List, Optional

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach: Dynamic programming with memoization to store results of subproblems.
        Time Complexity: O(n*m), where n is the number of coins and m is the target amount.
        Space Complexity: O(m), for storing the memoized results.
        """
        # Create a list to store the minimum number of coins needed for each amount from 0 to the target
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case, we need 0 coins to make 0 amount

        # Iterate over each coin and update the dp list accordingly
        for coin in coins:
            for i in range(coin, amount + 1):
                # If using the current coin results in a smaller number of coins than the current minimum,
                # update the minimum number of coins needed for this amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return the minimum number of coins needed to make the target amount, or -1 if it's not possible
        return dp[amount] if dp[amount] != float('inf') else -1

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # Expected: 3 (11 = 5 + 5 + 1)
    print(s.coinChange([2], 3))  # Expected: -1
    print(s.coinChange([1], 0))  # Expected: 0