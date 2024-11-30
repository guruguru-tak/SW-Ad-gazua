from collections import deque

t = int(input())


def bfs(grid, y, x, n, visited):
    # 8방 탐색
    # dx = [1, 0, 0, -1, 1, -1, -1, 1]
    # dy = [0, 1, -1, 0, 1, -1, 1, -1]
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    q = deque()
    q.append((y,x))

    # 본인 위치 계산
    count = 1

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx
            if 0<=ny<n and 0<=nx<n:
                # 처음 큐에서 뻗어나가는 것만 카운트
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    count += 1
                    q.append((ny, nx))
                    visited[ny][nx] = True

    # 해당 지역만 count 리턴
    return count


for tc in range(1, t+1):
    n = int(input())

    grid = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    # 정사각형 세로 가로 곱 -> 직사각형 넓이
    # 가장 큰 넓이 출력 위한 변수
    max_count = 0
    # bfs 로 찾아서 count 세기?

    # 일단 첫 1부터 찾기
    for y in range(n):
        for x in range(n):
            # 계속 새로운 1 찾기
            if not visited[y][x] and grid[y][x] == 1:
                visited[y][x] = True
                result = bfs(grid, y, x, n, visited)

                max_count = max(max_count, result)

    print(f"#{tc} {max_count}")