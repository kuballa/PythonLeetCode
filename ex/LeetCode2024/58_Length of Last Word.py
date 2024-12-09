# @algorithm @lc id=58 lang=python3 
# @title length-of-last-word


from en.Python3.mod.preImport import *
# @test("Hello World")=5
# @test("   fly me   to   the moon  ")=4
# @test("luffy is still joyboy")=6
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        s = reversed(s)
        flag = False
        subtract = 0
        for i, j in enumerate(s):
            if j != ' ' and not flag:
                flag = True
                subtract = i
            if j == ' ' and flag:
                return i - subtract
        return length - subtract