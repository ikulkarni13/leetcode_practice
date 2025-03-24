# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if no child nodes, return
# switch left and right nodes
# recursively go to left node and switch
# recursively go to right node and switch

class Solution:
    def invertTreeChat(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.left == None and root.right == None:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root