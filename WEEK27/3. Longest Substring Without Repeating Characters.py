class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        charList = {}
        maxValue = 0
        first, last , L = 0 , 0 , len(s)

        while True:
            print(first,last)
            if last >= L :
                break
            if s[last] in s[first:last] :
                maxValue = max(maxValue , last-first)
                first = charList[s[last]]+1
                del charList[s[last]]

            charList[s[last]] = last
            last += 1

        return max(maxValue , last-first)
