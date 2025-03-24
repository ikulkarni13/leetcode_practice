class Solution:
    def maxProfitChad(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy_day = 0
        sell_day = 1
        max_profit = 0

        while buy_day < (len(prices) - 1):
            if sell_day == (len(prices) - 1):
                max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
                buy_day += 1
                sell_day = buy_day + 1
                continue

            if prices[sell_day] - prices[buy_day] <= 0:
                buy_day += 1
                sell_day = buy_day + 1
                continue
            
            max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
            sell_day += 1
        
        return max_profit