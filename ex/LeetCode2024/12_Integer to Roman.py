# @algorithm @lc id=12 lang=python3 
# @title integer-to-roman


from en.Python3.mod.preImport import *
# @test(3749)="MMMDCCXLIX"
# @test(58)="LVIII"
# @test(1994)="MCMXCIV"
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_dict = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9]
            ,["X", 10], ["XL", 40], ["L", 50], ["XC", 90]
            ,["C", 100], ["CD", 400], ["D", 500], ["CM", 900]
            ,["M", 1000]
        ]

        result = ""

        for i,j in symbol_dict[::-1]:
            if num // j:
                count = num // j
                result += (count * i)
                num %= j

        return result