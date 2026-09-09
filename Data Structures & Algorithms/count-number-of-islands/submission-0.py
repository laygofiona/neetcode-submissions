class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set([])
        count = 0
        def traverse(grid, r, c, visit):
            # edge cases
            ROW, COL = len(grid), len(grid[0])
            # if either r or c becomes negative or r, c reaches length(grid) 
            # if we had already visited a 1 
            # if we reached water or 0
            # return --> stop exploring
            if (min(r, c) < 0 or r == ROW or c == COL or (r, c) in visit or grid[r][c] == "0"):
                return

            visit.add((r, c))
            # keep exploring
            traverse(grid, r + 1, c, visit)
            traverse(grid, r - 1, c, visit)
            traverse(grid, r, c + 1, visit)
            traverse(grid, r, c - 1, visit)
        
        # only want to explore islands
        # we can start exploring when we reach a 1 and it isn't in visit
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c] == "1" and (r, c) not in visit):
                    traverse(grid, r, c, visit)
                    count += 1
        
        return count



        