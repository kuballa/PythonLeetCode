# @algorithm @lc id=121 lang=python3 
# @title best-time-to-buy-and-sell-stock


from en.Python3.mod.preImport import *
# @test([7,1,5,3,6,4])=5
# @test([7,6,4,3,1])=0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = prices[0]
        max_price = 0
        price_var = 0

        for price in prices[1:]:
            if price < low_price:
                low_price = price
                max_price = 0
            if price > max_price:
                max_price = price
                price_var = max(price_var, max_price - low_price)
        return price_var
