from collections import deque

n = int(input())


max_height = 0
grid = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max(row) for row in grid)


def bfs(x, y, h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and not visited[nx][ny] and grid[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))

result = 0
for h in range(max_height):
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                cnt += 1
    result = max(result, cnt)

print(result)