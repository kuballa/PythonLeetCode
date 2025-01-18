# @algorithm @lc id=128 lang=python3 
# @title longest-consecutive-sequence


from en.Python3.mod.preImport import *
# @test([100,4,200,1,3,2])=4
# @test([0,3,7,2,5,8,4,6,0,1])=9
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d_nums = {}

        for x in nums:
            if x not in d_nums:
                d_nums[x] = 1
        
        p_dict = {}
        for x in d_nums:
            if x + 1 in d_nums or x - 1 in d_nums:
                p_dict[x] = 1
        if len(p_dict) > 0:
            max_num = max(p_dict)
            min_num = min(p_dict)
        else:
            max_num = 0
            min_num = 0

        counter = 1
        result = 1
        for x in range(min_num, max_num):
            if x + 1 in p_dict:
                counter += 1
                result = max(result, counter)
            else:
                result = max(result, counter)
                counter = 0
        
        return result if len(d_nums) > 1 else 1