class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        self.count = 0
        def bfs(node , s):
            s += node.val
            if s == targetSum : 
                self.count += 1
            if node.left :
                bfs(node.left , s)
            if node.right:
                bfs(node.right , s)

        q = [root]
        while q:
            node = q.pop()
            if node is None:
                continue

            bfs(node , 0)
            if node.right:
                q.append(node.right)
            if node.left :
                q.append(node.left)
        
        return self.count
