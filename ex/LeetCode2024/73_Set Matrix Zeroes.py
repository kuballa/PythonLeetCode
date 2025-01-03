# @algorithm @lc id=73 lang=python3 
# @title set-matrix-zeroes


from en.Python3.mod.preImport import *
# @test([[1,1,1],[1,0,1],[1,1,1]])=[[1,0,1],[0,0,0],[1,0,1]]
# @test([[0,1,2,0],[3,4,5,2],[1,3,1,5]])=[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix[0])
        b = len(matrix)
        temp = {}

        for x in range(b):
            temp[x] = []
            for y in range(r):
                if matrix[x][y] == 0:
                    temp[x].append(y)

        for i in temp:
            for j in temp[i]:
                for k in range(0, r):
                    matrix[i][k] = 0
                for k in range(0, b):
                    matrix[k][j] = 0