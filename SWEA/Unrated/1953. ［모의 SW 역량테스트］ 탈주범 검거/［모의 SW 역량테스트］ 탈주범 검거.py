# 1시간에 1범위 퍼진다 -> bfs 알고리즘
from collections import deque

t = int(input())


def bfs(grid, grid_x, grid_y, hole_x, hole_y, time_depth):
    visited = [[False]*grid_x for _ in range(grid_y)]

    q = deque()
            # (맨홀 y,x, 깊이(레벨, 현재 걸린 시간))
    q.append((hole_y, hole_x, 1))

    visited[hole_y][hole_x] = True

    # 시작 위치 포함
    total_count = 1

    while q:
        y, x, time = q.popleft()

        # print(grid[y][x])
        # 다음 큐 체크 위해 break 아닌 continue
        if time >= time_depth:
            continue

        # 7가지 터널 구조물 체크
        if grid[y][x] == 1:
            # 상우좌하 있으면 연결
            dx = [0, 1, -1, 0]
            dy = [-1, 0, 0, 1]
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0<=nx<grid_x and 0<=ny<grid_y:
                    if not visited[ny][nx]:
                        # 상
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 5 or grid[ny][nx] == 6:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time+1))
                        # 우
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 6 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time+1))
                        # 좌
                        elif i == 2:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 4 or grid[ny][nx] == 5:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))
                        # 하
                        elif i == 3:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 4 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

        elif grid[y][x] == 2:
            # 상하 있으면 연결
            dx = [0, 0]
            dy = [-1, 1]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 상
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 5 or grid[ny][nx] == 6:
                                visited[ny][nx] = True
                                total_count += 1
                                # print(ny, nx, grid[ny][nx], time)
                                q.append((ny, nx, time + 1))
                        # 하
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 4 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

        elif grid[y][x] == 3:
            # 우좌 있으면 연결
            dx = [1, -1]
            dy = [0, 0]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 우
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 6 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))
                        # 좌
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 4 or grid[ny][nx] == 5:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))
        elif grid[y][x] == 4:
            # 상우 있으면 연결
            dx = [1, 0]
            dy = [0, -1]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 우
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 6 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

                        # 상
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 5 or grid[ny][nx] == 6:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

        elif grid[y][x] == 5:
            # 하우 있으면 연결
            dx = [0, 1]
            dy = [1, 0]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 하
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 4 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))
                        # 우
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 6 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

        elif grid[y][x] == 6:
            # 하좌 있으면 연결
            dx = [0, -1]
            dy = [1, 0]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 하
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 4 or grid[ny][nx] == 7:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

                        # 좌
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 4 or grid[ny][nx] == 5:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

        elif grid[y][x] == 7:
            # 좌상 있으면 연결
            dx = [-1, 0]
            dy = [0, -1]
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < grid_x and 0 <= ny < grid_y:
                    if not visited[ny][nx]:
                        # 좌
                        if i == 0:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 3 or grid[ny][nx] == 4 or grid[ny][nx] == 5:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))
                        # 상
                        elif i == 1:
                            if grid[ny][nx] == 1 or grid[ny][nx] == 2 or grid[ny][nx] == 5 or grid[ny][nx] == 6:
                                visited[ny][nx] = True
                                total_count += 1
                                q.append((ny, nx, time + 1))

    return total_count

for tc in range(1, t+1):

    grid_y, grid_x, hole_y, hole_x, time_depth = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(grid_y)]

    result = bfs(grid, grid_x, grid_y, hole_x, hole_y, time_depth)

    print(f"#{tc} {result}")