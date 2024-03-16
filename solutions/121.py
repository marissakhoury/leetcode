"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Time Complexity: O(n), where n is the number of days (length of `prices` list).
Space Complexity: O(1). 
"""

def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, (price - min_price))
        min_price = min(min_price, price)
    return max_profit


if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    max_profit1 = max_profit(prices1)
    assert max_profit1 == 5
    print('Passed!')

    prices2 = [7,6,4,3,1]
    max_profit2 = max_profit(prices2)
    assert max_profit2 == 0
    print('Passed!')
