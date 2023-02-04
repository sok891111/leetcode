class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        if sum(nums) < target :
            return 0

        first,last = 0 , 0

        result = float('inf')
        total = nums[0]
        while first < len(nums) :
            
            if total >= target :
                result = min(result, last-first+1)
                if first == last and last < len(nums) -1 :
                    last += 1
                    total += nums[last]
                else:
                    total -= nums[first]
                    first +=1
                continue

            if last < len(nums) -1 :
                last += 1
                total += nums[last]
            else :
                total -= nums[first]
                first += 1

        return result
