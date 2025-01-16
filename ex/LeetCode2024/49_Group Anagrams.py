# @algorithm @lc id=49 lang=python3 
# @title group-anagrams


from en.Python3.mod.preImport import *
# @test(["eat","tea","tan","ate","nat","bat"])=[["bat"],["nat","tan"],["ate","eat","tea"]]
# @test([""])=[[""]]
# @test(["a"])=[["a"]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s_dict = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in s_dict:
                s_dict[sorted_s].append(s)
            else:
                s_dict[sorted_s] = []
                s_dict[sorted_s].append(s)
        
        return [s_dict[k] for k in s_dict]