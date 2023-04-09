class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        S = sum(nums) 
        if S % 2 != 0 :
            return False
        target = S //2
        possible = set()
        for num in nums:
            tmp = []
            for p in possible:
                tmp.append(p + num)
            for p in tmp : 
                possible.add(p)
            possible.add(num)
            if target in possible:
                return True

        return False
