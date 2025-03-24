class Solution:
    # brute force (get all profits, return greatest), O(n^2)
    # iterate through prices
    # iterate through prices from current i to end
    # if the current profit is greater than max_profit, reassign max_profit
    # return max profit

    # examples
    # prices = [7,1,5,3,6,4]
    # [1, 1, 1...100]

    # edge case
    # if len(prices) is 1, return 0

    # elegant
    # initialize buy_day and sell_day and max_profit
    # while anchor is not equal to prices length minus 1
    # check current profit
    # when profit is less than or equal to 0 increment anchor and runner
    # otherwise we have a valid profit
    # reassign max_profit
    # increment runner
    # if runner is equal to last index, increment anchor and reassign runner
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