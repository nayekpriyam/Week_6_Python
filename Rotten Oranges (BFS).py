from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    time = 0
    while q:
        r, c, t = q.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t+1))
                time = t+1
    return time if fresh==0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid)) 