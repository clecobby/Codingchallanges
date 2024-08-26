class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricetobuy=prices[0]
        profit=0
        for p in prices[1:]:
            if pricetobuy > p:
                pricetobuy= p
            
            profit=max(profit,p-pricetobuy)
        
        return profit
