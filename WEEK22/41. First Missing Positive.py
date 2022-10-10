class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lmax = max(nums)
        if lmax < 0 :
            return 1
        m = [False]*(len(nums)+1)
        m[0] = True
        for num in nums:
            if num > 0 and len(m) > num :
                m[num] = True
        
        for index, visited in enumerate(m):
            if visited == False:
                return index
            
        return lmax+1
