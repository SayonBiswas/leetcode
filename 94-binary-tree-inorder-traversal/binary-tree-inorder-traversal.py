# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        visited = []
        def inorder(root):
            if root is not None:
                inorder(root.left)
                visited.append(root.val)
                inorder(root.right)
            return
        inorder(root)
        return visited