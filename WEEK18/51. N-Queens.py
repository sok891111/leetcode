class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans=[]
        def nQueens( current ,not_allowed , array ):
            
            
            
            if current[0] > n :
                return 
            
            
            if current in not_allowed :
                return 
            
            
            
            row = ''
            for index in range(n):
                if index == current[1] :
                    row += 'Q'
                else:
                    row += '.'
            
            array.append(row)
            
            
            if len(array) == n :
                ans.append(array)
                return
            
            for index in range( 1 , n - current[0]):
                
                not_allowed.append( (current[0]+index , current[1]) )
                not_allowed.append( (current[0]+index , current[1]+index ) )
                not_allowed.append( (current[0]+index , current[1]-index ) )
              
            for index in range(n):
                nQueens( (current[0]+1 , index ) ,not_allowed[:], array[:] )
            
        
        for index in range(n):
            nQueens((0,index) , [], [])    
        return ans
