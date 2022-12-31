class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]* len(nums)
        dp[0] = nums[0]
        lastNegative = -1
        if nums[0] < 0 :
            lastNegative = 0
        for index in range(1, len(nums)):

            if nums[index] < 0 and lastNegative  > -1 :
                tmp = 1
                for j in range(lastNegative , index+1):
                    tmp *= nums[j]
                dp[index] = max(dp[lastNegative-1]*tmp , tmp , nums[index])
            else:
                dp[index] = max(nums[index] * dp[index-1],nums[index])

            if nums[index] < 0:
                lastNegative = index
            
        return max(dp)
