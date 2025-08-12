# URL: https://leetcode.com/problems/coin-change/description/

def coinchange(coins: list[int], amount: int) -> int:

    dp=[amount+1]*(amount+1)
    # amount+1 represents infinity (unreachable)
    dp[0] = 0
    # initialized to 0 (0 coins to get 0 amount)

    for i in range(1, amount+1):
        # for each cell in the dynamic programming
        for coin in coins:
            if i-coin>= 0:
                # for each coin, if the substraction is positive -> it is possible to
                # use that coin for amount value
                dp[i] = min(dp[i], dp[i-coin]+1)
                # use the number of coins of dp[i-coin] + another one since it is possible
                # to use that coin again
        
    return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == "__main__":

    print(coinchange([1,2,5], 11))
    print(coinchange([2],3))
    print(coinchange([1], 0))