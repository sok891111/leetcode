class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        cache = {}
        def backtracking(s):
            result = 0
            if s in cache:
                return cache[s]

            if not s :
                return 1
            
            if 0 < int(s[0]) < 10 :
                result += backtracking(s[1:])
            if 10<= int(s[0:2]) < 27 :
                result += backtracking(s[2:])
            cache[s] = result
            
            return result

        return backtracking(s)
        
