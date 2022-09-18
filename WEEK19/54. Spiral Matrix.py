class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row,col = len(matrix) , len(matrix[0])
        check= [[ False for _ in range(col)] for _ in range(row)]
        result = []
        d = [(0,1), (1,0) , (0,-1) , (-1,0)]
        
        def backtracking(x , y, index):
            if x >= row or y >= col:
                return
            
            if check[x][y] == True:
                return            
            result.append(matrix[x][y])
            check[x][y] = True
            
            new_x , new_y = x+ d[index][0] , y +d[index][1]
            
            if new_x >= row or new_y >= col or check[new_x][new_y] == True:
                index = (index+1) % 4
                new_x , new_y = d[index][0] + x , d[index][1] + y    
            backtracking(new_x,new_y , index)
                
        backtracking(0,0,0)
        return result
            
        
