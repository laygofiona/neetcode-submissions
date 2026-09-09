# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case: if we don't have a root
        if(not root):
            return []
        
        # initialize our deque with the root at col 0
        queue = deque([(root, 0)])
        # keep track of min_col and max_col for returning list of lists
        min_col, max_col = 0, 0
        # make a way to keep track of which nodes belong to which col
        # using a sortedDict
        cols = defaultdict(list)

        # iterature through our queue
        while queue:
            # get the item out from the queue
            # pop the item, extract the node, col
            node, col = queue.popleft()

            # add the node to our cols sortedDict
            cols[col].append(node.val)

            # update min_col and max_col
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            # check if node has any children
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                # add that to queue for processing
                queue.append((node.right, col + 1))
           
        

        res = []
        for col in range(min_col, max_col + 1):
            res.append(cols[col])
        
        return res


        
