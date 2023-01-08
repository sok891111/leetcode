class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        L = len(nums)
        result = []

        for i in range(L):
            for j in range(i+1 , L):
                left ,right = j+1 , L-1
                while True :

                    if left >= right :
                        break

                    current = nums[i] + nums[j] + nums[left] + nums[right]

                    if current > target : 
                        right -= 1
                    if current < target : 
                        left += 1
                
                    if current == target : 
                        tmp = (nums[i]  , nums[j]  , nums[left] , nums[right] )
                        if tmp not in result:
                            result.append( tmp )
                        right -= 1 
                        left += 1
        return result
