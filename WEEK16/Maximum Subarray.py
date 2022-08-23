class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        for index in range(1,len(nums)):
            
            if dp[index-1] + nums[index] > nums[index] :
                dp[index] = dp[index-1] + nums[index]
            else:
                dp[index] = nums[index]
        return max(dp)
