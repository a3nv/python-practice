def buy_sell(arr):
    best_profit, current_max = 0, 0
    for price in arr[::-1]:  # reversed(arr)
        current_max = max(current_max, price)
        profit = current_max - price
        best_profit = max(profit, best_profit)
    return best_profit


if __name__ == "__main__":
    print(buy_sell([9, 11, 8, 5, 7, 10]))  # 5
