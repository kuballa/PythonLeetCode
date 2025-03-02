# @algorithm @lc id=64 lang=python3 
# @title minimum-path-sum


from en.Python3.mod.preImport import *
# @test([[1,3,1],[1,5,1],[4,2,1]])=7
# @test([[1,2,3],[4,5,6]])=12
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid) - 1, len(grid[0]) - 1
        for i in range(row, -1, -1):
            for j in range(col, -1, -1):
                if (i,j) == (row, col):
                    continue
                elif i == row:
                    grid[i][j] += grid[i][j + 1]
                elif j == col:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]