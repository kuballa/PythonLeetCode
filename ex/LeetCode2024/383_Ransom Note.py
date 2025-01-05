# @algorithm @lc id=383 lang=python3 
# @title ransom-note


from en.Python3.mod.preImport import *
# @test("a","b")=false
# @test("aa","ab")=false
# @test("aa","aab")=true
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = {}

        for x in magazine:
            dict_mag[x] = dict_mag.get(x, 0) + 1

        for x in ransomNote:
            if x in dict_mag:
                dict_mag[x] -= 1
                if dict_mag[x] < 0:
                    return False
            if x not in dict_mag:
                return False
        
        return True