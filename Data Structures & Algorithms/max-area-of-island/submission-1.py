class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = float("-inf")

        def formIsland(grid, r, c) -> int:
            visited = set()
            def DFS(grid, r, c, visited):
                ROWS = len(grid)
                COLS = len(grid[0])

                # check (r,c) if out of bounds, alr visited, or 0
                if (r == ROWS or c == COLS or min(r, c) < 0):
                    return 0
                if ((r, c) in visited or grid[r][c] == 0):
                    return 0
               
                
                visited.add((r, c))
                added_area = 0 
                added_area += DFS(grid, r - 1, c, visited)
                added_area += DFS(grid, r + 1, c, visited)
                added_area += DFS(grid, r, c - 1, visited)
                added_area += DFS(grid, r, c + 1, visited)

                if grid[r][c] == 1:
                    added_area += 1

                return added_area
            
            return DFS(grid, r, c, visited)

        # go through eaceh cell and check if 1
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col] == 1):
                    max_area = max(formIsland(grid, row, col), max_area)
        # if no island exists return 0
        res = max(max_area, 0)
        return res
        
        