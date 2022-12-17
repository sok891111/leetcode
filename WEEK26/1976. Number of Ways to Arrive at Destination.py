class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        result = 0
        dp = [1]*n
        adj = [[] for _ in range(n)]
        
        for (s,d,w) in roads:
            adj[s].append((d,w))
            adj[d].append((s,w))

        
        distance = [float('inf')] * n
        visited = [False]*n
        distance[0] = 0
        q=[]
        heappush(q,(0,0))
        
        while q :
            a = list(heappop(q))[1]

            if visited[a] :
                continue
            visited[a] = True
             
            for (d,w) in adj[a]:
                if distance[a] + w < distance[d]:
                    distance[d] = distance[a] + w
                    heappush(q, (distance[d] , d))
                    dp[d] = dp[a]

                elif distance[a] + w == distance[d]:   
                    dp[d] += dp[a]

        return dp[-1]%(10**9 + 7)

        
        
