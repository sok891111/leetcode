class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x : x[0])
        start, end = intervals[0]
        result = []
        for interval in intervals:
            if interval[0] <= end:
                if interval[1] >= end : 
                    end = interval[1]
            else:
                result.append([start,end])
                start , end = interval
        else :
            result.append([start,end])                
        return result
        
