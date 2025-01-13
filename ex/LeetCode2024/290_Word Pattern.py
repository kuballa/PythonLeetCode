# @algorithm @lc id=290 lang=python3 
# @title word-pattern


from en.Python3.mod.preImport import *
# @test("abba","dog cat cat dog")=true
# @test("abba","dog cat cat fish")=false
# @test("aaaa","dog cat cat dog")=false
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = {}
        s_dict = {}

        for i, p in enumerate(pattern):
            if p not in p_dict:
                p_dict[p] = []
                p_dict[p].append(i)
            else:
                p_dict[p].append(i)

        s_split = s.split()
        for i, elem in enumerate(s_split):
            if elem not in s_dict:
                s_dict[elem] = []
                s_dict[elem].append(i)
            else:
                s_dict[elem].append(i)

        if len(p_dict) == len(s_dict):
            for p_key, s_key in zip(p_dict, s_dict):
                print(p_dict[p_key], s_dict[s_key])
                if p_dict[p_key] != s_dict[s_key]:
                    return False
        else:
            return False
        return True