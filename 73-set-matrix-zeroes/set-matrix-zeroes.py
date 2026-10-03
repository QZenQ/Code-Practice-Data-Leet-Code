class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstColZero = False

        for row in range(len(matrix)):

            if(matrix[row][0] == 0): isFirstColZero = True

            for col in range(1, len(matrix[0])):
                if(matrix[row][col] == 0):
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in matrix:
            print(*row)

        for row in range(len(matrix) - 1, -1, -1):
            for col in range(1, len(matrix[0])):
                if(matrix[row][0] == 0 or matrix[0][col] == 0):
                    matrix[row][col] = 0
            if(isFirstColZero): matrix[row][0] = 0

        for row in matrix:
            print(*row)
            
        