# @algorithm @lc id=36 lang=python3 
# @title valid-sudoku


from en.Python3.mod.preImport import *
# @test([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])=true
# @test([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])=false
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_numbers = {"1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1}

        for row in board:
            temp_numbers = {}
            for col in row:
                if col in valid_numbers:
                    temp_numbers[col] = temp_numbers.get(col, 0) + 1
                    if temp_numbers[col] > 1:
                        return False

        for col in zip(*board):
            temp_numbers = {}
            for row in col:
                if row in valid_numbers:
                    temp_numbers[row] = temp_numbers.get(row, 0) + 1
                    if temp_numbers[row] > 1:
                        return False
                        
        # Extract the 9 3x3 matrices
        submatrices = [
            [row[col:col+3] for row in board[row_start:row_start+3]]
            for row_start in range(0, 9, 3)
            for col in range(0, 9, 3)
        ]

        # Print the 3x3 matrices
        for submatrix in submatrices:
            temp_numbers = {}
            for row in [element for row in submatrix for element in row]:
                if row in valid_numbers:
                    temp_numbers[row] = temp_numbers.get(row, 0) + 1
                    if temp_numbers[row] > 1:
                        return False
        return True