# @algorithm @lc id=389 lang=python3 
# @title find-the-difference


from en.Python3.mod.preImport import *
# @test("abcd","abcde")="e"
# @test("","y")="y"
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s = {}

        for elem in s:
            dict_s[elem] = dict_s.get(elem, 0) + 1

        for i in range(len(t)):
            if t[i] in dict_s and dict_s[t[i]] > 0:
                dict_s[t[i]] -= 1
            else:
                return t[i]
        