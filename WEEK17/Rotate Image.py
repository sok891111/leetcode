class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        for row in range(n):
            for col in range(row+1,n) :
                matrix[row][col]  , matrix[col][row] = matrix[col][row] , matrix[row][col]
                
        # col swap
        for row in range(n):
            for col in range(n//2):
                matrix[row][col]  , matrix[row][n-col-1]= matrix[row][n-col-1] , matrix[row][col]
