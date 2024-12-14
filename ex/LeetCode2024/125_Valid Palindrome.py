# @algorithm @lc id=125 lang=python3 
# @title valid-palindrome


from en.Python3.mod.preImport import *
# @test("A man, a plan, a canal: Panama")=true
# @test("race a car")=false
# @test(" ")=true
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s if x.isalpha() or x.isdigit()]).lower()

        # for i in range(len(s) // 2):
        #     if s[i] != s[-(i + 1)]:
        #         return False
        # return True
        return s == s[::-1]