# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # check if there is a path to the right
        # if yes, keep going right and explore
        # check if ther eis a path to the left
        # if yes, keep going left and explore
        # best stores the diameter
        best = 0
        def traverse(root):
            nonlocal best
            if not root:
                # height of an empty subtree
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            best = max(best, left + right)

            # returns the max height
            return max(left, right) + 1

           
        traverse(root)
        return best

        
        