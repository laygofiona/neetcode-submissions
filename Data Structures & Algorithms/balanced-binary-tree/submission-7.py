# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMaxH(self, root):
        if (root == None):
            return 0
        
        
        h_Left = self.findMaxH(root.left) + 1
        h_Right = self.findMaxH(root.right) + 1
        
        if h_Left == h_Right:
            return h_Left

        return max(h_Left, h_Right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        max_L = self.findMaxH(root.left)
        max_H = self.findMaxH(root.right)

        diff = abs(max_L - max_H)
        if diff > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)