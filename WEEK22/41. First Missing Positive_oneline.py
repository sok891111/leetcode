class Solution(object):
    def firstMissingPositive(self, nums):
        return min(set(range(1,len(nums)+2)) - set(nums))
