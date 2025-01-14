# @algorithm @lc id=242 lang=python3 
# @title valid-anagram


from en.Python3.mod.preImport import *
# @test("anagram","nagaram")=true
# @test("rat","car")=false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d_dict = {}

        for i in s:
            d_dict[i] = d_dict.get(i, 0) + 1

        for i in t:
            if i in d_dict and d_dict[i] > 0:
                d_dict[i] -= 1
            else:
                return False
        return True