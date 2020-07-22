# This is just a simple recursion implementation of the problem.


def maximum_profit(price, start, end):
    if end <= start:
        return 0

    profit = 0
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] + maximum_profit(price, start, i - 1) + maximum_profit(price, j + 1,
                                                                                                         end)
                day_to_buy.append(i)
                profit = max(profit, curr_profit)
    return profit


if __name__ == '__main__':
    day_to_buy = []
    n = int(input())
    prices = [int(i) for i in input().split()]
    print(maximum_profit(prices, 0, n - 1))
    print(day_to_buy[-1])