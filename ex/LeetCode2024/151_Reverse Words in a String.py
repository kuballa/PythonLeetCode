# @algorithm @lc id=151 lang=python3 
# @title reverse-words-in-a-string


from en.Python3.mod.preImport import *
# @test("the sky is blue")="blue is sky the"
# @test("  hello world  ")="world hello"
# @test("a good   example")="example good a"
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        output = ''

        for i in range(len(words) - 1, -1, -1):
            if len(words[i]) > 0:
                output += words[i] + " "

        return output[:-1]