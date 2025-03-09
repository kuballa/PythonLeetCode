# @algorithm @lc id=9 lang=python3 
# @title palindrome-number


from en.Python3.mod.preImport import *
# @test(121)=true
# @test(-121)=false
# @test(10)=false
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = abs(x)
        reversed_num = 0
        while num:
            temp_num = num % 10
            num //= 10
            reversed_num = reversed_num * 10 + temp_num
        return reversed_num == x