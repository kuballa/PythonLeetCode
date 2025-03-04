# @algorithm @lc id=93 lang=python3 
# @title restore-ip-addresses


from en.Python3.mod.preImport import *
# @test("25525511135")=["255.255.11.135","255.255.111.35"]
# @test("0000")=["0.0.0.0"]
# @test("101023")=["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) > 12:
            return result

        def backtrack(i, dots, currIP):

            if dots == 4 and i == len(s):
                result.append(currIP[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, currIP + s[i:j + 1] + ".")
        backtrack(0, 0, "")
        return result