class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        L = len(nums)
        start,end , mid = 0, L -1 , 0
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                print(mid)
                break           
            if nums[mid] < target :
                start = mid +1
            else:
                end = mid - 1
        else:
            return [-1,-1]
            
        start , end = mid, mid

        while True:
            if start < 0 or nums[start] != target :
                start += 1
                break
            else :
                start -= 1

        while True:
            if end == L or nums[end] != target :
                end -= 1
                break
            else :
                end += 1
        return [start,end]



##### python 의 bisect 활용

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        L = len(nums) -1

        left = bisect_left(nums, target)
        if left > L or nums[left] != target:
            return [-1,-1]
        
        right = bisect_right(nums, target)
        return [left, right-1]
