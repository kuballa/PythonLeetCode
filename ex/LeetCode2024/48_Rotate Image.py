# @algorithm @lc id=48 lang=python3 
# @title rotate-image


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[[7,4,1],[8,5,2],[9,6,3]]
# @test([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])=[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            r -= 1
            l += 1