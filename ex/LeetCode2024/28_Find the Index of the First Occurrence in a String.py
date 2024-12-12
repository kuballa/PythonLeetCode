# @algorithm @lc id=28 lang=python3 
# @title find-the-index-of-the-first-occurrence-in-a-string


from en.Python3.mod.preImport import *
# @test("sadbutsad","sad")=0
# @test("leetcode","leeto")=-1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i] == needle[0]:
                flag = True
                j = 0
                while flag:
                    if haystack[i + j] != needle[j]:
                        flag = False
                        break
                    j += 1
                    if j == len(needle):
                        return(i)
        return -1