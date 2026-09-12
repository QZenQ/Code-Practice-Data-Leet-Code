class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        layer = 0
        n = len(matrix)
        while layer < n//2:
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                top = matrix[first][i]

                #top
                matrix[first][i] = matrix[last - offset][first]
                #left
                matrix[last - offset][first] = matrix[last][last - offset]
                #bottom
                matrix[last][last - offset] = matrix[i][last]
                #right
                matrix[i][last] = top

            layer +=1