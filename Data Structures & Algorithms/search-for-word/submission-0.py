class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(grid, r, c, visit, currIdx, word):
            ROWS, COLS = len(grid), len(grid[0])

            # Base cases
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] != word[currIdx]:
               return 0

            if currIdx == len(word) - 1 and board[r][c] == word[currIdx]:
                # complete word found
                return 1
            
            # otherwise continue searching
            visit.add((r, c))
            currIdx += 1
            validWordCount = 0

            validWordCount += dfs(grid, r + 1, c, visit, currIdx, word)
            validWordCount += dfs(grid, r - 1, c, visit, currIdx, word)
            validWordCount += dfs(grid, r, c + 1, visit, currIdx, word)
            validWordCount += dfs(grid, r, c - 1, visit, currIdx, word)

            visit.remove((r, c))
            return validWordCount
            
        ROWS, COLS = len(board), len(board[0])
        firstLettersPos = []
        # find cells where val is equal to first letter in word
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    # put cell pos (r, c) in arr
                    firstLettersPos.append((r, c))
                
        # perform dfs on each (r, c) in arr
        for pos in firstLettersPos:
            r = pos[0]
            c = pos[1]
            # if returned value from dfs > 0 -> return true
            if dfs(board, r, c, set(), 0, word) > 0:
                return True

        # otherwise after checking each (r, c) in dfs, return false
        return False