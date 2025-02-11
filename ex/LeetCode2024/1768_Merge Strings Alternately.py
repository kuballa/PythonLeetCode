# @algorithm @lc id=1894 lang=python3 
# @title merge-strings-alternately


from en.Python3.mod.preImport import *
# @test("abc","pqr")="apbqcr"
# @test("ab","pqrs")="apbqrs"
# @test("abcd","pq")="apbqcd"
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l, r = 0, 0
        i = 0

        while l < len(word1) and r < len(word2):
            if i % 2 == 0:
                result += word1[l]
                l += 1
            else:
                result += word2[r]
                r += 1
            i += 1
        result += word1[l:]
        result += word2[r:]

        return result