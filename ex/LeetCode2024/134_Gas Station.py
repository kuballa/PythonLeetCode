# @algorithm @lc id=134 lang=python3 
# @title gas-station


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],[3,4,5,1,2])=3
# @test([2,3,4],[3,4,3])=-1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # journey_start = cost.index(min(cost))
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
                
        return res