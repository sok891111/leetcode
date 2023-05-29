class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if sum(costs) <= coins :
            return len(costs)
            
        costs.sort()
        result = 0
        for cost in costs:
            coins -= cost
            if coins < 0 :
                break
            result += 1

        return result
