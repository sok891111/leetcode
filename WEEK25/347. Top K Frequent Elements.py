class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        return sorted(count, key=count.get,reverse=True)[:k]
