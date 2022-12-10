class Solution:
    def max_profit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        for cur_price in prices:
            cur_profit = cur_price - lowest_price
            if lowest_price > cur_price:
                lowest_price = cur_price
            elif cur_profit > profit:
                profit = cur_profit
        return profit
