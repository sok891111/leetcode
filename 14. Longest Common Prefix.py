class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        index = 0
        stop = False
        min_val = min([len(s) for s in strs])
        while True : 
            cur = None    
            if min_val <= index:
                break
            for string in strs:
                if cur is not None and cur != string[index]:
                    stop = True
                    break
                cur = string[index]
            else:
                result += string[index]
            index += 1
            if stop :
                break

        return result
