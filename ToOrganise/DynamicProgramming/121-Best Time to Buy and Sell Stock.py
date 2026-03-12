### https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution(object):
    '''
    def maxProfit1(self, prices):
        res = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                res = max(prices[j] - prices[i], res)
        return res
    '''

    def maxProfit(self, prices):
        if not prices: return 0
        dp = prices[0]
        res = 0
        for i in range(len(prices)):
            res = max(prices[i] - dp, res)
            dp = min(dp, prices[i])
        return res

print(Solution().maxProfit([7,1,5,3,6,4]))
        
