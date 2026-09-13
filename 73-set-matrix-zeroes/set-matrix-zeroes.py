class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vr, vc, qr, qc = [], [], [], []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    if(i not in qr): qr.append(i)
                    if(j not in qc): qc.append(j)

        while(qr):       
            row = qr.pop(0)
            for i in range(len(matrix[0])):
                matrix[row][i] = 0

        while(qc):       
            col = qc.pop(0)
            for i in range(len(matrix)):
                matrix[i][col] = 0
