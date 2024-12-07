# @algorithm @lc id=13 lang=python3 
# @title roman-to-integer


from en.Python3.mod.preImport import *
# @test("III")=3
# @test("LVIII")=58
# @test("MCMXCIV")=1994
# @test("IV")=4
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I": 1
            ,"V": 5
            ,"X": 10
            ,"L": 50
            ,"C": 100
            ,"D": 500
            ,"M": 1000
        }
        
        sum_roman = 0

        for i in range(1, len(s)):
            if symbol_dict[s[i - 1]] >= symbol_dict[s[i]]:
                sum_roman += symbol_dict[s[i - 1]]
            else:
                sum_roman -= symbol_dict[s[i - 1]]
        sum_roman += symbol_dict[s[-1]]

        return sum_roman