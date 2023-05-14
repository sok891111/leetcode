class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        result = 0
        satisfaction.sort(reverse=True)
        dishes = []
        for dish in satisfaction :
            tmp = 0
            dishes.append(dish)
            L = len(dishes)
            for index , d in enumerate(dishes):
                tmp += (( L - index) * d)
                
            if tmp < result :
                break
            else :
                result = tmp
                
        return result
