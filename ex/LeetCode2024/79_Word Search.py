# @algorithm @lc id=79 lang=python3 
# @title word-search


import collections
from en.Python3.mod.preImport import *
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")=true
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")=true
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")=false
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            elif (0 > r or r >= ROW or
                  0 > c or c >= COL or
                  word[i] != board[r][c] or
                  (r, c) in visit):
                return False
            
            visit.add((r,c))
            result = (dfs(r + 1,c, i + 1) or
                      dfs(r - 1,c, i + 1) or
                      dfs(r,c + 1, i + 1) or
                      dfs(r,c - 1, i + 1))
            visit.remove((r, c))
            return result

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
        return False