# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root):
        if (root == None):
            return [True, 0]
        
        
        t_Left = self.traverse(root.left)
        t_Left[1] += 1
        t_Right = self.traverse(root.right)
        t_Right[1] += 1

        if abs(t_Left[1] - t_Right[1]) > 1:
            return [False, -1]
        if t_Right[0] == False or t_Left[0] == False:
            return [False, -1]
        
        return [True, max(t_Left[1], t_Right[1])]
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.traverse(root)
        return res[0]