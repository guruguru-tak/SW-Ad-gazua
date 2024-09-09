
t = int(input())

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def dfs(y, x):
    #종료 조건?

    global cnt

    for dist in range(4):
        ny, nx = y + dy[dist], x + dx[dist]
        if 0 <= ny < n and 0 <= nx < n:
            if(grid[y][x] + 1) == grid[ny][nx]:
                cnt += 1
                dfs(ny, nx)


for tc in range(1, t+1):
    n = int(input())

    grid = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    start_idx = 0


    #모든 y, x 탐색 필요
    for y in range(n):
        for x in range(n):
            # 자기 자신을 포함해서 1 시작
            cnt = 1
            dfs(y, x)

            if cnt > max_count or (cnt == max_count and grid[y][x] < start_idx):
                start_idx = grid[y][x]
                max_count = cnt
    print(f"#{tc} {start_idx} {max_count}")


