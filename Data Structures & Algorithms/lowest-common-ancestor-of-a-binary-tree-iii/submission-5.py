"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_visited = set()


        # collect nodes visited for p until it reaches the root
        while(p is not None):
            # append p to p_visited
            p_visited.add(p)
            # move p up
            p = p.parent

        # collect nodes visited for q until it reaches the root
        while(q is not None):
            # check if q is in p_visited
            if q in p_visited:
                return q
            q = q.parent
        

        return None
        
       
        