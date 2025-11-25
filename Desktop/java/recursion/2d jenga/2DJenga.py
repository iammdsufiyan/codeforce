from collections import deque, defaultdict
import copy

def jenga_min_cost(N, M, grid, target):
    piece_cells = defaultdict(list)
    for i in range(N):
        for j in range(M):
            val = grid[i][j]
            if val != 0:
                piece_cells[val].append((i,j))

    sides = ['up','down','left','right']
    min_cost = float('inf')
    best_side = ''

    def simulate(side):
        temp_grid = [row[:] for row in grid]
        removed = set()
        N_rows, M_cols = N, M
        changed = True

        while True:
            to_remove = set()
            # Determine scan order for this side
            if side=='up':
                rows = range(N_rows)
                cols = range(M_cols)
            elif side=='down':
                rows = range(N_rows-1,-1,-1)
                cols = range(M_cols)
            elif side=='left':
                rows = range(N_rows)
                cols = range(M_cols)
            else:  # right
                rows = range(N_rows)
                cols = range(M_cols-1,-1,-1)

            # Identify removable pieces along the side
            for i in rows:
                for j in cols:
                    val = temp_grid[i][j]
                    if val==0 or val in removed:
                        continue
                    cells = piece_cells[val]
                    # Check if piece is at edge for this side
                    if side=='up' and any(x==0 for x,_ in cells):
                        to_remove.add(val)
                    elif side=='down' and any(x==N_rows-1 for x,_ in cells):
                        to_remove.add(val)
                    elif side=='left' and any(y==0 for _,y in cells):
                        to_remove.add(val)
                    elif side=='right' and any(y==M_cols-1 for _,y in cells):
                        to_remove.add(val)

            if not to_remove:
                break

            # Remove pieces
            for val in to_remove:
                removed.add(val)
                for x,y in piece_cells[val]:
                    temp_grid[x][y]=0

            # Gravity propagation
            while True:
                gravity_removed = set()
                for val, cells in piece_cells.items():
                    if val in removed:
                        continue
                    for x,y in cells:
                        if temp_grid[x][y]==0:
                            continue
                        if x+1 < N_rows and temp_grid[x+1][y]==0:
                            gravity_removed.add(val)
                            break
                if not gravity_removed:
                    break
                for val in gravity_removed:
                    removed.add(val)
                    for x,y in piece_cells[val]:
                        temp_grid[x][y]=0

        return sum(removed)

    for side in sides:
        cost = simulate(side)
        if cost<min_cost:
            min_cost = cost
            best_side = side

    return min_cost, best_side

# ------------------------
# Input
# ------------------------
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
target = int(input())

cost, side = jenga_min_cost(N,M,grid,target)
print(f"{cost} via {side}")