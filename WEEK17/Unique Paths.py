class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row -1 >= 0 :
                    dp[row][col] += dp[row-1][col]
                if col -1 >= 0 :
                    dp[row][col] += dp[row][col-1]
        
        return dp[m-1][n-1]
