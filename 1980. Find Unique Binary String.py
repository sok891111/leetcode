class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        self.result = None
        L = len(nums)
        nums = set(nums)
        def backtracking(binaryString, level):
            
            if self.result is not None:
                return 
            
            if level == L :
                if not binaryString in nums:
                    self.result = binaryString
                return

            backtracking(binaryString+'0' , level+1)
            backtracking(binaryString+'1' , level+1)

        backtracking('',0)

        return self.result
