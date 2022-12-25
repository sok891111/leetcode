class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0

        if len(nums) < 2 :
            return nums[0]

        dp = [0]*len(nums)
        dp[0] , dp[1]  = nums[0] , max(nums[0],nums[1])

        for index in range(2,len(nums)):
            dp[index] = max(dp[index-2] + nums[index] , dp[index-1])

        return max(dp)
                
