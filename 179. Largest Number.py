class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        if sum(nums) == 0 :
            return '0'
                    
        L = len(nums) - 1
        nums = [str(num) for num in nums]

        for inx in range(L,0,-1):
            for inj in range(inx):
                if int(nums[inj] + nums[inj+1]) < int(nums[inj+1] + nums[inj]):
                    nums[inj+1] , nums[inj] = nums[inj] , nums[inj+1]

        return ''.join(nums)
        
