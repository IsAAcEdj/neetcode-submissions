class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSell = 0
        for i in range(len(prices) - 1):
            curSell = max(prices[i + 1:]) - prices[i]
            if(curSell > maxSell):
                maxSell = curSell
        return maxSell
