def maxProfit(prices):
    min_price = 1000
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        max0 = i - min_price
        max_profit = max(max0,max_profit)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))