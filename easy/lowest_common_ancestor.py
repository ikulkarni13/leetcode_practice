class Solution:
    def lowestCommonAncestorChad(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == None:
                return node
            
            if (node.val > p.val) and (node.val > q.val):
                return dfs(node.left)
            elif (node.val < p.val) and (node.val < q.val):
                return dfs(node.right)
            else:
                return node

        return dfs(root)