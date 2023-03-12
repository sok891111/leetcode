class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        L1 , L2 = len(s) , len(goal)
        if L1 != L2:
            return False

        dict1  = {} 
        for w in s : 
            if w in dict1.keys():
                dict1[w] += 1
            else:
                dict1[w] = 1
        
        if s == goal and max(dict1.values()) == 1 :
            return False

        count = 0
        for index, g in enumerate(goal) :
            if g in dict1.keys():
                dict1[g] -= 1
                if dict1[g] == 0:
                    del dict1[g]
            else:
                return False

            if s[index] != goal[index]:
                count +=1 

            if count > 2 :
                return False

        return True
