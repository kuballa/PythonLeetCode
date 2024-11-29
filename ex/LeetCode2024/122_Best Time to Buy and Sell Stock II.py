# @algorithm @lc id=122 lang=python3 
# @title best-time-to-buy-and-sell-stock-ii


from en.Python3.mod.preImport import *
# @test([7,1,5,3,6,4])=7
# @test([1,2,3,4,5])=4
# @test([7,6,4,3,1])=0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_lp = 0
        lp = prices[0]
        prev_mp = 0
        mp = 0
        p = 0
        p_sum = 0

        for i in prices[1:]:
            prev_lp = lp
            prev_mp = mp

            if i < lp:
                lp = i
                mp = 0
            if i > mp:
                mp = i
                p = max(p, mp - lp)
            elif i <= mp:
                p_sum += p
                lp = i
                mp = i
                p = 0
        p_sum += p

        return p_sum