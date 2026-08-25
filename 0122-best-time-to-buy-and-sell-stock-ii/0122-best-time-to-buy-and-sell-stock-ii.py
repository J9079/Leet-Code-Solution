class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        max_profit=0
        sum=0
        while i<len(prices) and j<len(prices):
          if prices[i]>prices[j]:
            i+=1
            j+=1
            continue
          else:
            profit=prices[j]-prices[i]
            max_profit=max(profit,max_profit)
            sum+=profit  
            j+=1
          i+=1  
        return sum