"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

from functools import cache
from typing import List

# solution using Dynamic Programming table
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for index in range(len(coins))] for index in range(amount+1)]
        
        for index in range(len(coins)):
            dp[0][index] = 1 # 1 ways to make up amount 0 with any set of coins
        
        for coin_index in range(len(coins)):
            for amount_index in range(1, amount+1): # do not update amount = 0
                if amount_index - coins[coin_index] >= 0:
                    # possible to use coin

                    # take previous result
                    dp[amount_index][coin_index] = dp[amount_index-coins[coin_index]][coin_index]

                # check if result index exists if this coin is not used at all
                if coin_index - 1 >= 0:
                    # add those combinations into total
                    dp[amount_index][coin_index] += dp[amount_index][coin_index-1]
        
        print(dp)
        return dp[amount][len(coins)-1]

# this solution works as well
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        # returns the number of combinations
        # @cache is IMPORTANT for improving runtime performance
        @cache
        def recursionHelper(coin_index, amount):
            # BASE CASES
            if amount == 0:
                # reached possible combination
                return 1
            if coin_index == len(coins):
                # no more possible coins
                return 0

            # 2 actions, continue taking the same coin OR move on to next coin
            take_coin = 0
            if (amount - coins[coin_index] >= 0):
                # possible to take coin
                take_coin = recursionHelper(coin_index, amount-coins[coin_index])
            skip_coin = recursionHelper(coin_index+1, amount)

            return take_coin + skip_coin

        return recursionHelper(0, amount)