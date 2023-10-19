class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-1] * len(prices)
        dp[0] = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i])
            if(prices[i] - dp[i] > profit):
                profit = prices[i] - dp[i]
        return profit
        