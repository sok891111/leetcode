class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        N, M = len(word1) +1 , len(word2) +1
        dp = [[0] * N for _ in range(M)]

        for index in range(N):
            dp[0][index] = index

        for index in range(M):
            dp[index][0] = index            

        for i in range(1, M) :
            for j in range( 1, N) :
                diff = 1
                if word1[j-1] == word2[i-1]:
                    diff= 0
                dp[i][j] = min (  dp[i][j-1] +1 , dp[i-1][j] +1  , dp[i-1][j-1]+diff)       

        return dp[-1][-1]
