# @algorithm @lc id=224 lang=python3 
# @title basic-calculator


from en.Python3.mod.preImport import *
# @test("1 + 1")=2
# @test(" 2-1 + 2 ")=3
# @test("(1+(4+5+2)-3)+(6+8)")=23
class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: the current environment's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0
        return ans + sign * num