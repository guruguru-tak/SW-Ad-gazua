from collections import deque


def bfs(x, y):
    #델타 4방향, 3시방향 기준 시계방향
    #우, 하, 좌, 상
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()

        #4방향 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

t = int(input())

for _ in range(t):

    #가로 번호(열), 세로 번호(행), 배추 심은 위치의 갯수
    m, n, lo = map(int, input().split())

    #배추농장 초기화
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    #배추위치 표시
    for _ in range(lo):
        x, y = map(int, input().split())
        grid[y][x] = 1 #x = 열, 가로로 y = 행, 세로 따라서 행 열 순 = [y][x]


    count = 0
    for i in range(n): #n = 행, 세로
        for j in range(m):#m = 열 , 가로
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
