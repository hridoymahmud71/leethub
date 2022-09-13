class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        globalMax = 0
        buyPrice = prices[0]

        for i in range(1,len(prices)):

            if prices[i] < buyPrice:
                buyPrice = prices[i]

        
            elif (prices[i] - buyPrice) > globalMax :
                globalMax = prices[i] - buyPrice

        return globalMax