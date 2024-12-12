# @algorithm @lc id=6 lang=python3 
# @title zigzag-conversion


from en.Python3.mod.preImport import *
# @test("PAYPALISHIRING",3)="PAHNAPLSIIGYIR"
# @test("PAYPALISHIRING",4)="PINALSIGYAHRPI"
# @test("A",1)="A"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res