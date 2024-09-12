"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List

# DP solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for index in range(amount+1)] # need to include (index = amount)
        dp[0] = 0 # 0 coins needed for 0 amount of money

        for index, coins_used in enumerate(dp):
            # index represents the amount of money needed
            for coin in coins:
                if coin <= index:
                    # possible to use coin
                    if dp[index-coin] != -1 and dp[index] != -1:
                        # existing results, do comparison
                        dp[index] = min(dp[index-coin]+1, dp[index])
                    elif dp[index-coin] != -1:
                        # no current result for amount=index
                        dp[index] = dp[index-coin]+1
                    # otherwise, no current or previous result, therefore do no updates

        return dp[amount]

# runtime of this solution is too slow
class SolutionRecursion:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins_used = [-1]
        def coinRecursionHelper(index, coins_used, amount_left, min_coins_used):
            if amount_left == 0:
                if coins_used < min_coins_used[0] or min_coins_used[0] == -1:
                    min_coins_used[0] = coins_used
                return

            if amount_left < 0 or index == len(coins):
                return

            if coins_used > min_coins_used[0] and min_coins_used[0] != -1:
                # more coins being used, discard case
                return

            # take the coin; coins used +1, reduce amount by coin value
            coinRecursionHelper(index, coins_used+1, amount_left-coins[index], min_coins_used)

            # skip the coin; move to next index coin
            coinRecursionHelper(index+1, coins_used, amount_left, min_coins_used)
        
        # run the helper
        coinRecursionHelper(0, 0, amount, min_coins_used)
        return min_coins_used[0]