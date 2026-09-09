class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # determine if row and column are valid
        
        
        # determine if row is valid
        for r in range(len(board)):
            rowSet = set()
            for c in range(len(board[0])):
                # goes through each element in row
                if(board[r][c] != "."):
                    if(board[r][c] in rowSet):
                        return False
                    else: 
                        rowSet.add(board[r][c])
        
        # determine if col is valid
        for c in range(len(board[0])):
            colSet = set()
            for r in range(len(board)):
                # goes through each element in row
                if(board[r][c] != "."):
                    if(board[r][c] in colSet):
                        return False
                    else: 
                        colSet.add(board[r][c])
        
        # determine if sub-boxes of the grid are valid
        corners = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        # go through each corner
        for corner in corners:
            box = set()
            # get starting row
            row = corner[0]
            # get starting col
            col = corner[1]

            max_r = row + 3
            max_c = col + 3

            while row < max_r:
                col = corner[1]
                while col < max_c:
                    if(board[row][col] != "."):
                        if(board[row][col] in box):
                            return False
                        else: 
                            box.add(board[row][col])
                    col += 1
                row += 1

        
        return True