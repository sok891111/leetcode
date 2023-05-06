class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        M, N = len(text1) , len(text2) 
        dp = [[0]*M for _ in range(N)]


        for n in range(N):
            for m in range(M):

                if text1[m] == text2[n] :
                    dp[n][m] = 1
                    if n-1 > -1 and m-1 > -1:
                        dp[n][m] += dp[n-1][m-1] 
                else:
                    n1 , n2 = 0,0
                    if n-1 > -1 :
                        n1 = dp[n-1][m]
                    if m-1 > -1 :
                        n2 = dp[n][m-1]
                    dp[n][m] = max( n1, n2)
        return dp[-1][-1]
