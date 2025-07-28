# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
Algorithm: Greedy + Tracking Min
"""

def bttbass(prices: list[int]) -> int:

    minprice = float("inf")
    maxprofit = 0

    for price in prices:
        if price < minprice:
            # best day to buy
            minprice = price
        else:
            profit = price - minprice
            maxprofit = max(maxprofit, profit)

    return maxprofit