class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSell = 0
        l = 0
        r = 1
        while r < len(prices):
            if(prices[r] > prices[l]):
                curSell = prices[r] - prices[l]
                if(curSell > maxSell):
                    maxSell = curSell
            else:
                l = r
            r += 1
        return maxSell
