class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        negative = False
        if x < 0 :
            negative = True
        x = list(str(abs(x)))
        x.reverse()
        result = int(''.join(x))
        if result < -2**31 or result > 2**31 -1 :
            return 0
        return result * -1 if negative else result
             

        
