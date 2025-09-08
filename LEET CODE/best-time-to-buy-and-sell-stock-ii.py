class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
if __name__ == "__main__":
    obj = Solution()
    arr=[1,2,3,4,5]
    arr.sort(reverse=False)
    print(obj.maxProfit(arr))







