from typing import List, Optional

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Approach: Dynamic programming
        Time Complexity: O(n*m)
        Space Complexity: O(n*m), where n is the number of denominations and m is the total amount.
        """
        # Create a table to store the minimum number of coins for each amount from 0 to the given amount
        dp = [float('inf')] * (amount + 1)
        
        # We need 0 coins to make 0 amount
        dp[0] = 0
        
        # For each coin denomination
        for coin in coins:
            # For each amount from the coin denomination to the given amount
            for x in range(coin, amount + 1):
                # Update the minimum number of coins for the current amount
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        # If we cannot make the given amount with any combination of coins, return -1
        if dp[amount] == float('inf'):
            return -1
        
        # Return the minimum number of coins for the given amount
        return dp[amount]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.change(10, [1, 2, 5]))  # Expected: 3
    print(s.change(0, [1, 2, 5]))  # Expected: 0
    print(s.change(11, [1, 2, 5]))  # Expected: -1