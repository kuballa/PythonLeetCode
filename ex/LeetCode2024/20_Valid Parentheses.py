# @algorithm @lc id=20 lang=python3 
# @title valid-parentheses


from en.Python3.mod.preImport import *
from collections import deque
# @test("()")=true
# @test("()[]{}")=true
# @test("(]")=false
# @test("([])")=true
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for par in s:
            if par in ["(","[","{"]:
                q.append(par)
            else:
                if not q:
                    return False
                curr = q.pop()
                if par == ")" and curr == "(":
                    continue
                elif par == "]" and curr == "[":
                    continue
                elif par == "}" and curr == "{":
                    continue
                else:
                    return False

        return True