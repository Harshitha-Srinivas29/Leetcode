class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p > min_price :
                profit = max(profit, p - min_price)
                print(profit)
        return profit
        