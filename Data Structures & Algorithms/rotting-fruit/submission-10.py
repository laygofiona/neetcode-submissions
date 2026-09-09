class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        # find rotten fruits
        # count number of fresh fruits --> keep track of if freshFruit count is reached
        foundRotten = False
        foundFresh = False
        fruitsToSpoil = 0
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 2:
                    # add rotten fruit to queue and visited hash set
                    visited.add((r, c))
                    queue.append((r, c))
                    foundRotten = True
                elif grid[r][c] == 1:
                    if foundFresh == False:
                        foundFresh = True
                    fruitsToSpoil += 1

        if foundRotten == False and foundFresh == False:
            return 0
        if foundRotten == False:
            return -1
        
        

        mins = -1

        fruitsSpoiled = 0
        while queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visited or grid[r + dr][c + dc] != 1:
                        continue
                    else:
                        fruitsSpoiled += 1
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))
            mins += 1
        if fruitsSpoiled < fruitsToSpoil:
            return -1
        return mins

        
