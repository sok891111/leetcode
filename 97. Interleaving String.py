class Solution(object):
    def isInterleave(self, s1, s2, s3):

        self.result = False
        mem = {}
        L1,L2,L3 = len(s1) , len(s2), len(s3)
        def backtracking( o ,s,t):

            if (o,s,t) in mem.keys() :
                return mem[(o,s,t)]

            if o >= L1 and s >= L2 and t >= L3:
                self.result = True
                return True

            if o >= L1 and s>= L2 and t < L3 :        
                return False

            if t >= L3:
                return False

            if o < L1 and s1[o] == s3[t]:
                result = backtracking(o+1 , s , t+1)
                mem[(o+1,s,t+1)] = result

            if self.result == True:
                return
                
            if s < L2 and s2[s] == s3[t]:
                result = backtracking(o , s+1 , t+1)
                mem[(o,s+1,t+1)] = result
                
        backtracking(0,0,0)
        return self.result
