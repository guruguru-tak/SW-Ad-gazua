from collections import deque
t = int(input())


def bfs(start_y, start_x, cut_Cnt, grid, n):
    # 시뮬레이션 설정위해 위치 설정
    # 방향 설정: 북(0), 동(1), 남(2), 서(3)
    dx = [-1, 0, 1, 0]  # y 좌표 변화량
    dy = [0, 1, 0, -1]  # x 좌표 변화량

    q = deque()
    # 시작 상태: 위치(y, x), 방향(dir), 남은 나무 베기 횟수(k_remaining), 조작 횟수(operations)
    # RC카는 항상 북쪽(0)을 바라보는 상태로 시작
    q.append((start_y, start_x, 0, cut_Cnt, 0))

    # # 방문 여부를 저장하기 위한 딕셔너리
    visited = dict()
    visited[(start_y, start_x, 0, cut_Cnt)] = 0

    while q:
        y, x, dir, k_remaining, operations = q.popleft()

        # 현재 위치가 목적지인 경우 조작 횟수 반환
        # 종료 조건
        if grid[y][x] == 'Y':
            return operations

        # 전진 액션// 0입력시 북쪽으로 전진 설정
        ny, nx = y + dx[dir], x + dy[dir]
        if 0 <= ny < n and 0 <= nx < n:
            cell = grid[ny][nx]
            if cell in ('G', 'Y'):
                next_state = (ny, nx, dir, k_remaining)
                # 방문하지 않았거나 더 적은 조작으로 도달 가능한 경우
                if next_state not in visited or visited[next_state] > operations + 1:
                    visited[next_state] = operations + 1
                    q.append((ny, nx, dir, k_remaining, operations + 1))
            elif cell == 'T' and k_remaining > 0:
                # 나무를 베고 전진하는 경우
                next_state = (ny, nx, dir, k_remaining - 1)
                if next_state not in visited or visited[next_state] > operations + 1:
                    visited[next_state] = operations + 1
                    q.append((ny, nx, dir, k_remaining - 1, operations + 1))
            # 그 외의 경우는 이동 불가

        # 좌회전 액션
        ndir = (dir + 3) % 4  # 왼쪽으로 90도 회전 => 동쪽 (1 + 3) % 4 => 0 왼쪽 90도 회전
        next_state = (y, x, ndir, k_remaining)
        if next_state not in visited or visited[next_state] > operations + 1:
            visited[next_state] = operations + 1
            q.append((y, x, ndir, k_remaining, operations + 1))

        # 우회전 액션
        ndir = (dir + 1) % 4  # 오른쪽으로 90도 회전
        next_state = (y, x, ndir, k_remaining)
        if next_state not in visited or visited[next_state] > operations + 1:
            visited[next_state] = operations + 1
            q.append((y, x, ndir, k_remaining, operations + 1))

        # 목표 지점에 도달할 수 없는 경우 -1 반환
    return -1


for tc in range(1, t+1):
    n, cut_Cnt = map(int, input().split())

    grid = [list(map(str, input().strip())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    # 시작 위치 찾기
    start_y, start_x = -1, -1
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'X':
                start_y, start_x = y, x
                break
        # 한 번만 체크하도록 설정
        if start_y != -1:
            break

    #  BFS 실행하여 최소 조작 횟수 계산
    result = bfs(start_y, start_x, cut_Cnt, grid, n)
    print(f"#{tc} {result}")

