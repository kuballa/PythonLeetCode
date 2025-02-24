# @algorithm @lc id=5 lang=python3 
# @title longest-palindromic-substring


from en.Python3.mod.preImport import *
# @test("babad")="bab"
# @test("cbbd")="bb"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(res, resLen, l, r, s):
            res = res
            resLen = resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            return res, resLen
        
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            res, resLen = isPalindrome(res, resLen, l, r, s)

            l, r = i, i + 1
            res, resLen = isPalindrome(res, resLen, l, r, s)

        return res