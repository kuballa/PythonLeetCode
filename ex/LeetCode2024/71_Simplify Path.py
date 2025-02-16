# @algorithm @lc id=71 lang=python3 
# @title simplify-path


from en.Python3.mod.preImport import *
# @test("/home/")="/home"
# @test("/home//foo/")="/home/foo"
# @test("/home/user/Documents/../Pictures")="/home/user/Pictures"
# @test("/../")="/"
# @test("/.../a/../b/c/../d/./")="/.../b/d"
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)