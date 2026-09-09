# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trav(root, node):
        # we've found node in the tree
        if(root == node):
            return True
        if(not root):
            return False
        
        return Solution.trav(root.left, node) or Solution.trav(root.right, node)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        pathDiverged = False
        while not pathDiverged:
            # check the right subtree first
            # check if p and q is in the right subtree
            if(Solution.trav(curr.right, p) == True and Solution.trav(curr.right, q) == True):
                # if it is, then move curr to right child
                curr = curr.right
            # check if p and q is in left subtree
            elif(Solution.trav(curr.left, p) == True and Solution.trav(curr.left, q) == True):
                # if it is, then move curr to left child
                curr = curr.left
            # otherwise, either p is in left and q is in right, or p is in right and q is in left
            else:
                # aka their paths have diverged
                return curr
        
        return root
        
        