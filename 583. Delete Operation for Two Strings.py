class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        L,M = len(word1) +1 , len(word2) +1
        dp = [[0]*L for _ in range(M)]

        for index in range(L):
            dp[0][index] = index
        for index in range(M):
            dp[index][0] = index        

        for i in range(1,M):
            for j in range(1,L):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1] , dp[i-1][j] ) + 1
                    
        return dp[-1][-1]        
