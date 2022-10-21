class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(row):
            
            if len(row) < 1:
                return False
            
            mid = len(row)//2
            
            if row[mid] == target:
                return True
            if row[mid] < target:
                return search(row[mid+1:])
            if row[mid] > target:
                return search(row[:mid])
            
        for row in matrix:
            if row[0] > target:
                continue
            if search(row) == True:
                return True
