class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_to_integer = {
            'I' : 1,
            'V' : 5, 
            'X' : 10,
            'L' : 50 , 
            'C' : 100 , 
            'D' : 500,
            'M' : 1000
        }

        result = 0
        prev = float('inf')
        for roman_number in s :
            integer = roman_to_integer[roman_number]
            if prev < integer :
                result -= ( prev * 2)    
            result += integer
            prev = integer

        return result
