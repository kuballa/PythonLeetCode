# @algorithm @lc id=205 lang=python3 
# @title isomorphic-strings


from en.Python3.mod.preImport import *
# @test("egg","add")=true
# @test("foo","bar")=false
# @test("paper","title")=true
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i, x in enumerate(s):
            if x in dict_s:
                dict_s[x].append(i)
            else:
                dict_s[x] = []
                dict_s[x].append(i)

        for i, x in enumerate(t):
            if x in dict_t:
                dict_t[x].append(i)
            else:
                dict_t[x] = []
                dict_t[x].append(i)

        for x, y in zip(dict_s, dict_t):
            if not dict_s or not dict_t:
                return False
            if dict_s[x] != dict_t[y]:
                return False
        return True