# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

# 모든땅 다 체크하면 시간초과
# 네트워크 퍼지듯 이동값 +1 씩 증가로 저장하고, 모든 grid 내 값 계산하기

t = int(input())


def bfs(visited, q, n, m):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue

            # 다음 이동 위치(ny, nx)가 전 위치(cy, cx)의 값이
            # 이동해서 +1인 값보다 크면 (ny, nx)의 값이(ex: 무한대)거나
            # , 큰 값이면 작은 값 갱신
            if visited[ny][nx] > visited[cy][cx] + 1:
                visited[ny][nx] = visited[cy][cx] + 1
                # 처음 전체 물 위치 + 앞으로 완탐할 땅 위치 전부 큐에 추가해서
                # 현재 +1해서 2인 위치라면 다음 +1 인 3인 땅을 체크해야 하기에 전부 추가
                q.append((ny, nx))

    # 모든 visited 배열 값 전부 더해서 리턴값 반환
    move_sum = 0
    for vy in range(n):
        for vx in range(m):
            move_sum += visited[vy][vx]

    return move_sum

for tc in range(1, t+1):
    n, m = map(int, input().split())

    grid = [list(map(str, input().strip())) for _ in range(n)]

    # 방문처리
    visited = [[10**18] * m for _ in range(n)]

    total_Cnt = 0

    # walk = [[10**18] * m for _ in range(n)]

    # 모든 물 좌표 먼저 담아서 보내주기기
    q = deque()

    for y in range(n):
        for x in range(m):
            # 물일때만 확인으로 시간 줄이기기
            if grid[y][x] == "W":
                visited[y][x] = 0
                q.append((y, x))

    total_Cnt = bfs(visited, q, n, m)


    print(f"#{tc} {total_Cnt}")