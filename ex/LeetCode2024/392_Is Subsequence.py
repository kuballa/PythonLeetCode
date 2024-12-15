# @algorithm @lc id=392 lang=python3 
# @title is-subsequence


from en.Python3.mod.preImport import *
# @test("abc","ahbgdc")=true
# @test("axc","ahbgdc")=false
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        sub_idx = 0
        while idx < len(t) and sub_idx < len(s):
            if s[sub_idx] == t[idx]:
                sub_idx += 1
            idx += 1
        return sub_idx == len(s)