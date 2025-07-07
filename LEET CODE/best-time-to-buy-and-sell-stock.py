class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximumProfit=0
        i=0
        j=1
        profit_achieved_days={}
        # for i,price in enumerate(prices):
        while i < len(prices) and j < len(prices):
            profit=prices[j] - prices[i]
            if (profit) < 0:
                i=j
            elif profit>maximumProfit:
                maximumProfit=profit
            j+=1
        return maximumProfit
stock=[7,1,5,3,6,4]
obj=Solution()
print(obj.maxProfit(stock))

                
                
