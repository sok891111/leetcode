class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for _ in range(n)]
        min_height = float('inf')
        result = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        def dfs(start):
            q = collections.deque()
            q.append(start)
            visited = set()
            distance = [0]*n
            while q :
                v = q.popleft()
                for node in adj[v]:
                    if node not in visited:
                        q.append( node )  
                        distance[node] = max(distance[node] , distance[v]+1)
                visited.add(v)

            return distance

        
        result = [float('inf')]* n
        dist1 = dfs(0)
        left = dist1.index(max(dist1))
        dist2 = dfs(left)
        
        
        right = dist2.index(max(dist2))
        dist3 = dfs(right)

        
        for index in range(n):
            if index == left or index == right :
                continue
            result[index] = max(dist2[index] , dist3[index])

        
        min_val = min(result)

        return [index for index, val in enumerate(result) if val == min_val  ]
