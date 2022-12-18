class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        L = len(s)+1
        dp =[False]*L
        dp[0] = True
        for index in range(L):
            for word in wordDict:
                if index - len(word) >= 0 :
                    if dp[index-len(word)] == True and s[index-len(word) : index] == word :
                        dp[index] = True
                        break
        return dp[-1]
