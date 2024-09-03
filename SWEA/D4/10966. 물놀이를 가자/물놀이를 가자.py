from collections import deque
#1000 * 1000 => 배열 L 모든 탐색은 10**14 승으로 런타임 에러나게 된다.

t = int(input())


def bfs(visited, q, n, m):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    #각 큐 좌표에 4방 탐색
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #벽
            if 0 <= nx < m and 0 <= ny < n:
            # if 0 > nx or nx > m or 0 > ny or ny > n: continue
            #다음 이동 위치(ny, nx)가 전 위치(y, x)의 값이
            # 이동해서 +1인 값보다 크면 (ny, nx)의 값이(ex: 무한대)거나
            # , 큰 값이면 작은 값 갱신
                if visited[ny][nx] > visited[y][x]+1:
                    visited[ny][nx] = visited[y][x]+1
                    #처음 전체 물 위치 + 앞으로 완탐할 땅 위치 전부 큐에 추가해서
                    #현재 +1해서 2인 위치라면 다음 +1 인 3인 땅을 체크해야 하기에 전부 추가
                    q.append((ny, nx))

    #
    move_sum = 0
    for vy in range(n):
        for vx in range(m):
            move_sum += visited[vy][vx]

    return move_sum





for tc in range(1, t+1):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    visited = [[10**18]*m for _ in range(n)]
    #결과 담을 변수
    result = 0

    # 모든 물 위치 큐에 넣어 한 번에 처리하면 시간 초과 안난다
    q = deque()
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 'W':
                visited[y][x] = 0
                q.append((y, x))

    result = bfs(visited, q, n, m)

    print(f"#{tc} {result}")

