# @algorithm @lc id=209 lang=python3 
# @title minimum-size-subarray-sum


from en.Python3.mod.preImport import *
# @test(7,[2,3,1,2,4,3])=2
# @test(4,[1,4,4])=1
# @test(11,[1,1,1,1,1,1,1,1])=0
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res