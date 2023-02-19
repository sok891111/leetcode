class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L = len(nums)
        dp = [0] * L

        dp[0] = 1

        for inx in range(1,L):
            maxLength = 0
            for inj in range(inx):
                if nums[inj] < nums[inx]:
                    maxLength = max(maxLength , dp[inj])
            dp[inx] = maxLength + 1

        return max(dp)
