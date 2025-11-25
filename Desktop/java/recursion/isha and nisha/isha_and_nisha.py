import sys
sys.setrecursionlimit(10000)

def read_tokens():
    for line in sys.stdin:
        for tok in line.strip().split():
            yield tok

def in_rect(r, c, rect):
    x1,y1,x2,y2 = rect
    return x1 <= r <= x2 and y1 <= c <= y2

def main():
    tokens = read_tokens()
    try:
        N = int(next(tokens))
    except StopIteration:
        return
    M = int(next(tokens))
    grid = [['']*(M+1) for _ in range(N+1)]  
    for i in range(1, N+1):
        for j in range(1, M+1):
            grid[i][j] = next(tokens)

    I = int(next(tokens))
    clues = {}
    for _ in range(I):
        T = int(next(tokens))
        x1 = int(next(tokens)); y1 = int(next(tokens))
        x2 = int(next(tokens)); y2 = int(next(tokens))
        if T not in clues:
            clues[T] = []
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        clues[T].append((x1,y1,x2,y2))

    word = next(tokens)
    L = len(word)
    starts = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if grid[i][j] == word[0]:
                starts.append((i,j))
    if not starts:
        print("Impossible")
        return

    visited = [[False]*(M+1) for _ in range(N+1)]
    best = float('inf')
    found_any = False

    def violations_at(r, c, t):
        if t not in clues:
            return 0
        cnt = 0
        for rect in clues[t]:
            if in_rect(r,c,rect):
                cnt += 1
        return cnt

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    
    def dfs(r, c, idx, cur_viol):
        nonlocal best, found_any
       
        if cur_viol >= best:
            return
        
        if idx == L-1:
           
            found_any = True
            if cur_viol < best:
                best = cur_viol
            return
       
        ni = idx + 1
        for dr,dc in dirs:
            rr = r + dr
            cc = c + dc
            if rr < 1 or rr > N or cc < 1 or cc > M: continue
            if visited[rr][cc]: continue
            if grid[rr][cc] != word[ni]: continue
            add = violations_at(rr, cc, ni+1)
            visited[rr][cc] = True
            dfs(rr, cc, ni, cur_viol + add)
            visited[rr][cc] = False
           
            if best == 0:
                return

   
    for (sr,sc) in starts:
        init_add = violations_at(sr, sc, 1)
        
        if init_add >= best:
            continue
        visited[sr][sc] = True
        dfs(sr, sc, 0, init_add)
        visited[sr][sc] = False
        if best == 0:
            break

    if not found_any:
        print("Impossible")
    else:
        if best == 0:
            print("All clues are correct")
        else:
            print(best)

if __name__ == "__main__":
    main()