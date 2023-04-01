class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        dp = [[0]*L for _ in range(L)]
        max_val = 1
        index = (0,0)
        for i in range(L) :
            dp[i][i] = 1

        for i in reversed(range(L)) :
            for j in range(L-1 ,i, -1):
                if s[i] == s[j] and ( dp[i+1][j-1] > 0  or i+1 > j-1 ):
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > max_val:
                        max_val = dp[i][j]
                        index = (i,j)
                        
        return s[index[0] : index[1]+1]
