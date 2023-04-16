class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i][j] => i,j 까지의 가로 길이
        R , C = len(matrix) , len(matrix[0])
        dp = [ [0]*C for _ in range(R)]
        result = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == "1" :
                    dp[i][j] = dp[i][j-1] + 1
                    y_val = 1
                    x_val = dp[i][j]
                    
                    while True:
                        result = max(result, x_val*y_val)  
                        if i - y_val < 0 :
                            break
                        if matrix[i- y_val][j] != "1" :
                            break
                        x_val = min(x_val , dp[i - y_val][j] )
                        y_val += 1
                        
                    
        return result
