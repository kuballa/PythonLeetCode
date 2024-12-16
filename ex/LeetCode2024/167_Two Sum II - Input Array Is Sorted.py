# @algorithm @lc id=167 lang=python3 
# @title two-sum-ii-input-array-is-sorted


from en.Python3.mod.preImport import *
# @test([2,7,11,15],9)=[1,2]
# @test([2,3,4],6)=[1,3]
# @test([-1,0],-1)=[1,2]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            two_sum = numbers[low] + numbers[high]
            if two_sum < target:
                low += 1
            elif two_sum > target:
                high -= 1
            else:
                return [low + 1, high + 1]