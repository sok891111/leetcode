class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        result = [True]
        adj = [[] for _ in range(numCourses)]
        nodeList = dict.fromkeys(set([i for _ in prerequisites for i in _]), 0)
        ts = []
        for course, prerq in prerequisites :
            if course == prerq:
                return False
            else:
                adj[prerq].append(course)
                
        visited = [False]*numCourses
        def dfs(node):
            if nodeList[node] == 1:
                result[0] = False
            
            
            if visited[node]  == True:
                return 
            
            nodeList[node] = 1
            visited[node] = True
            for u in adj[node]:
                dfs(u)
        
            nodeList[node] = 2
            ts.append(node)
            
        for node in nodeList:
            dfs(node)  
        
        return result[0]
