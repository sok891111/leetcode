"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node or node is None :
            return None
            
        visited = []
        adjList = []
        stack = [node]
        while stack :
            current = stack.pop()
            if current in visited or not current :
                continue

            for n in current.neighbors:
                stack.append(n)
                while len(adjList) < n.val :
                    adjList.append([])
                adjList[current.val-1].append(n.val)
            visited.append(current)
        
        if not adjList :
            return Node(1,None)


        nodes = [ Node(index+ 1 , [] ) for index, _ in enumerate(adjList)] 
        for index, adj in enumerate(adjList):
            for n in adj:
                nodes[index].neighbors.append( nodes[n-1])

        return nodes[0]
