# @algorithm @lc id=3 lang=python3 
# @title longest-substring-without-repeating-characters


from en.Python3.mod.preImport import *
# @test("abcabcbb")=3
# @test("bbbbb")=1
# @test("pwwkew")=3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res