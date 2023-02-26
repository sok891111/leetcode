class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M,N = len(grid) , len(grid[0])
        distance = [[float('inf')] *N for _ in range(M) ]  
        visited = [[False] *N for _ in range(M) ]  
        q = []
        distance[0][0] = grid[0][0]
        heappush(q, (0, (0,0)))

        while q :
            x,y = list(heappop(q))[1]

            if visited[x][y] :
                continue
            visited[x][y] = True

            if y+1 < N and distance[x][y] + grid[x][y+1] < distance[x][y+1] :
                distance[x][y+1] = distance[x][y] + grid[x][y+1]
                heappush(q, ( distance[x][y+1], (x, y+1) ))

            if x+1 < M and distance[x][y] + grid[x+1][y] < distance[x+1][y] :
                distance[x+1][y] = distance[x][y] + grid[x+1][y]
                heappush(q, ( distance[x+1][y], (x+1, y) ))                


        return distance[-1][-1]
