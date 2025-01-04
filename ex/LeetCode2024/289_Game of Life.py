# @algorithm @lc id=289 lang=python3 
# @title game-of-life


from en.Python3.mod.preImport import *
# @test([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])=[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# @test([[1,1],[1,0]])=[[1,1],[1,1]]
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board[0])
        b = len(board)
        res = {}

        for x in range(r):
            for y in range(b):
                res[(y,x)] = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if y + i < 0 or y + i >= b or x + j < 0 or x + j >= r or (y + i == y and x + j == x):
                            continue
                        else:
                            res[y,x].append(board[y + i][x + j])

        for i in res:
            sum_of_life = sum(res[i])
            if sum_of_life < 2:
                board[i[0]][i[1]] = 0
            elif sum_of_life > 3 and board[i[0]][i[1]] == 1:
                board[i[0]][i[1]] = 0
            elif sum_of_life == 3 and board[i[0]][i[1]] == 0:
                board[i[0]][i[1]] = 1