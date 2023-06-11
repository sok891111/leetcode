class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L = len(s)
        if L <= numRows or numRows == 1:
            return s      
        
        rows = ['']*numRows
        index , m, n= 0 , 0 ,0

        while index < L :
            rows[m] += s[index]
            if m < numRows-1 and n%(numRows-1) == 0 :
                m += 1
            else:
                m -= 1
                n += 1
            index+= 1
        
        return ''.join(rows)
        
            
