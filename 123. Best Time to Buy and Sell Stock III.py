class Solution(object):
    def maxProfit(self, prices):

        L = len(prices)
        base = [0] * L
        minPrice = -prices[0]
        base[0] = -prices[0]
        
        for index in range(1,L):
            minPrice = max(minPrice , -prices[index])
            base[index] = minPrice

        buy1 = [0] * L
        for index in range(1,L):
            buy1[index] = max(buy1[index-1] , prices[index] + base[index-1] )
        
        buy2 = [0] * L
        maxDiff = -prices[0]
        for index in range(1,L):
            buy2[index] = max(buy2[index-1] , prices[index] + maxDiff )            
            maxDiff = max(maxDiff , buy1[index-1] - prices[index] )

        return buy2[-1]
