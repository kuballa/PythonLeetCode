# @algorithm @lc id=8 lang=python3 
# @title string-to-integer-atoi


from en.Python3.mod.preImport import *
# @test("42")=42
# @test(" -042")=-42
# @test("1337c0d3")=1337
# @test("0-1")=0
# @test("words and 987")=0
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = -1 if s[0] == "-" else 1
        if s[0] in {'-', '+'}:
            s = s[1:]

        num = 0
        for c in s:
            if not c.isdigit():
                break
            num *= 10 + int(c)
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 -1:
                return 2**31 - 1
        return sign * num