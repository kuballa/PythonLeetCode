# @algorithm @lc id=14 lang=python3 
# @title longest-common-prefix


from en.Python3.mod.preImport import *
# @test(["flower","flow","flight"])="fl"
# @test(["dog","racecar","car"])=""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_length = 200
        for i in strs:
            min_length = min(len(i), min_length)

        prefix = ''
        character = ''
        flag = True
        for i in range(min_length):
            character = strs[0][i]
            for j in range(len(strs)):
                if character != strs[j][i]:
                    flag = False
            if flag:
                prefix += strs[0][i]
            else:
                break
        
        return prefix
