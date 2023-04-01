class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        result = 0
        L = len(isConnected)
        visited=[False]*L
        for node in range(L):
            q=[]
            # if node not in visited:
            if not visited[node]:
                result += 1
                q.append(node)
                while q :

                    current = q.pop(0)
                    if visited[current]:
                        continue
                    visited[current] = True
                    
                    for next , value in enumerate(isConnected[current]):
                        if value == 1:
                            q.append(next)
                    
        return result
