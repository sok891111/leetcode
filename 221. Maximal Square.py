class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        M,N = len(matrix) , len(matrix[0])
        dp = [ [0] * N for _ in range(M)]
        result = 0

        for m in range(M):
            for n in range(N):
                if matrix[m][n] ==  '1' :
                    dp[m][n] = 1
                    if result == 0 :
                        result = 1
                else:
                    continue
                
                if ( m-1 > -1 and n-1 > -1 ) and dp[m-1][n-1] > 0 :
                    height = int(dp[m-1][n-1] ** 0.5)                       
                    w, h = 0 , 0
                    for index in range(m, m-height-1 , -1):
                        if matrix[index][n] != '1' :
                            break
                        w += 1
                    for index in range(n, n-height-1 , -1):
                        if matrix[m][index] != '1' :
                            break
                        h += 1
                    dp[m][n] = min(h,w) ** 2
                    result = max(result, dp[m][n])
        return result
                    
