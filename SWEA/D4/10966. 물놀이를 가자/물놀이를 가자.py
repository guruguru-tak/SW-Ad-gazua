from collections import deque

t = int(input())


def bfs(q, walk, n, m):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue

            # 만약 내가 다음이동 값이 현재 값이 이동해서 +1인 값보다 크면 최소 걸음 아님
            # 시작지 처음 무한대로 시작해 최소값을 게속 대입해줌
            if walk[ny][nx] > walk[cy][cx] + 1:
                walk[ny][nx] = walk[cy][cx] + 1
                q.append((ny, nx))

    # walk 최소 걸음수 저장 배열에 입력된 총 최소 걸음수 보내준다
    cnt = 0
    for y in range(n):
        for x in range(m):
            cnt += walk[y][x]

    return cnt


for tc in range(1, t+1):
    n, m = map(int, input().split())

    grid = [list(map(str, input().strip())) for _ in range(n)]

    # 최소 걸음 수 저장 방문 배열
    walk = [[10**18]*m for _ in range(n)]

    q = deque()

    total_walk = 0

    for y in range(n):
        for x in range(m):
            if grid[y][x] == "W":
                # 출발지 0
                walk[y][x] = 0
                # 모든 물 출발지 큐에 먼저 담기
                q.append((y,x))

    total_walk = bfs(q, walk, n, m)

    print(f"#{tc} {total_walk}")
