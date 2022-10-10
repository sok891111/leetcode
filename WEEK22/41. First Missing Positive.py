class Solution(object):
    def firstMissingPositive(self, nums):
        m = [False]*(len(nums)+1)
        m[0] = True
        for num in nums:
            if num > 0 and len(m) > num :
                m[num] = True
        
        for index, visited in enumerate(m):
            if visited == False:
                return index
            
        return max(nums)+1
