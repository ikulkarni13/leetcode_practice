class Solution:
    def diameterOfBinaryTreeChad(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node):
            nonlocal max_diameter

            if node == None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_diameter = max(max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        
        dfs(root)
        return max_diameter