from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        counter_t = defaultdict(int)
        L  = len(s)
        for letter in t:
            counter_t[letter] += 1
        
        q = []
        counter_finder = defaultdict(int)
        left, right = -1 , -1
        find = list(t)
        for index, letter in enumerate(s):

            if letter in find:
                find.pop(find.index(letter))

            if letter in t :    
                counter_finder[letter] += 1
                if left < 0 :
                    left = index
                else:
                    q.append(index)


            if not find :
                right = index
                break
        if right < 0 :
            return ''

        
        min_val = right-left
        result = s[left:right+1]

        while q :
            
            
            find = s[left]
            left = q.pop(0)
            counter_finder[find] -= 1
            if counter_finder[find] >=  counter_t[find]:            
                if right < L :
                    if right-left < min_val:
                        min_val = right-left
                        result = s[left:right+1]
                continue
            
            while True:
                
                right +=1 

                if right >= L :
                    break

                

                if s[right] in t :
                    counter_finder[s[right]] += 1
                    q.append(right)

                if s[right] == find : 
                    
                    if right-left < min_val:
                        min_val = right-left
                        result = s[left:right+1]
                    break

                
