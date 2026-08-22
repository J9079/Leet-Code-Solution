class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        max_profits=0
        while i<len(prices) and j<len(prices):
          if prices[i]>prices[j]:
            prices[i]=prices[j]
            j+=1
            continue
          else:
            profit=prices[j]-prices[i]
            max_profits=max(profit,max_profits)
            j+=1
        return max_profits        