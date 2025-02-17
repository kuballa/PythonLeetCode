# @algorithm @lc id=150 lang=python3 
# @title evaluate-reverse-polish-notation


from en.Python3.mod.preImport import *
# @test(["2","1","+","3","*"])=9
# @test(["4","13","5","/","+"])=6
# @test(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])=22
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            else:
                stack.append(int(token))
        return stack[0]