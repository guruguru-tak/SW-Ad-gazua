from collections import deque

t = int(input())


def bfs(grid, n):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    # 최소비용을 기록할 벡터
    time = [[10**18]*n for _ in range(n)]
    # 시작점의 비용은 arr[0][0]
    time[0][0] = grid[0][0]

    # BFS를 위한 deque
    # deque([ ]) -> 형식으로 iterable 형식으로 인자 받을 수 있다.
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if ny < 0 or nx < 0 or nx >= n or ny >= n: continue

            new_time = time[y][x] + grid[ny][nx]

            # 한칸 넘어갈 시간 보다 더 적은 비용으로 이동할 수 있을 때만 갱신
            if new_time < time[ny][nx]:
                time[ny][nx] = new_time
                q.append((ny, nx))

    # 목표 지점까지의 최소 비용 반환
    return time[n-1][n-1]

for tc in range(1, t+1):
    n = int(input())

    grid = [list(map(int, input().strip())) for _ in range(n)]

    # print(grid)

    # bfs를 이용하요 최소 비용 계산
    result = bfs(grid, n)

    print(f"#{tc} {result}")
