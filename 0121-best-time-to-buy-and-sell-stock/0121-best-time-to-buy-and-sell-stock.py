class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        curr_min = prices[0]
        for i in range(len(prices)-1):
            if curr_min > prices[i]:
                curr_min = prices[i]
            else:
                result = max(result, prices[i]-curr_min)
        return result

        