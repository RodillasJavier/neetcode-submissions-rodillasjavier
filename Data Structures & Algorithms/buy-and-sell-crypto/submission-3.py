class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        in:
            - int[] prices
            - prices[i] = price of coin on day i
        out:
            - max profit you can achieve
            - 0 allowed
        constraints:
            - can only buy or sell once on each day (not both)
            - 1 <= prices.length <= 100
            - 0 <= prices[i] <= 100
        '''
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                new_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, new_profit)
            else:
                buy = sell

            sell += 1

        return max_profit

# time complexity: O(n)
# space complexity: O(1)