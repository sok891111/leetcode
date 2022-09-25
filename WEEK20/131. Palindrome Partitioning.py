class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        def checkPlindrome(s):
            left, right = 0 , len(s)-1
            while(True):
                if left >= right:
                    return True
                
                if s[left] == s[right] :
                    left += 1
                    right -=1
                else:
                    return False
        
        
        def backtracking(s , substring):
            
            if s == '':
                result.append(substring)    
                return 
            tmp = []
            for index in range(len(s)):
                check = s[:index+1]
                if checkPlindrome(check) == False:
                    continue
                
                tmp = substring[:]
                tmp.append(check)
                backtracking(s[index+1:] , tmp)
                
        backtracking(s,[])
        return result
