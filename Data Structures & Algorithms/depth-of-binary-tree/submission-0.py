# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dep = 0
        q = deque()
        if root:
            q.append(root)
        
        while len(q) > 0:
            dep += 1
            for i in range(len(q)):
                proc = q.popleft()
                if proc.right:
                    q.append(proc.right)
                if proc.left:
                    q.append(proc.left)
        
        return dep


