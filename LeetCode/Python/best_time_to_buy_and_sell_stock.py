# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
Algorithm: Greedy + Tracking Min
"""

def bttbass(prices: list[int]) -> int:

    minprice = float("inf")
    # if no purchase possible return 0
    maxprofit = 0

    for price in prices:
        if price < minprice:
            # if a better purchase day is found
            minprice = price
        else:
            # a good day selling is found
            profit = price - minprice
            maxprofit = max(maxprofit, profit)

    return maxprofit

if __name__ == "__main__":

    print(bttbass([7,1,5,3,6,4]))
    print(bttbass([7,6,4,3,1]))