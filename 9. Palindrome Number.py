class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 :
            return False


        tmp , number , d = x, 0 , 0
        
        while tmp > 0 :
            d += 1
            tmp = tmp // 10

        tmp = x
        while tmp > 0 :
            number += (tmp % 10) * 10**(d-1)
            tmp = tmp // 10
            d -= 1
        
        return number == x
