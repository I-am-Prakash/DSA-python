def buyAndSellStock(arr):
    profit = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            profit = max(profit, arr[j]-arr[i])
    return profit

# print(buyAndSellStock([10,6,3,11,13]))
print(buyAndSellStock([10,9,8,6,2]))
# tc-> O(n^2)
# sc => o(1)


def buyAndSellStock(arr):
    min_price = float('inf')
    max_profit = 0

    for price in arr:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit


# print(buyAndSellStock([10,6,3,11,13]))
print(buyAndSellStock([10,9,8,6,2]))
# tc-> O(n)
# sc => o(1)
