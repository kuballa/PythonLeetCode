# @algorithm @lc id=200 lang=python3 
# @title number-of-islands


import collections
from en.Python3.mod.preImport import *
# @test([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])=1
# @test([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])=3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        result = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < ROW and
                        0 <= c < COL and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    result += 1
        return result