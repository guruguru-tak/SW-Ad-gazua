from collections import deque

t = int(input())

def bfs(y, x, visited, grid, n):


    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    q = deque()
    # 행열 값도 넣어줘야 하지 않나?
    q.append((y, x, (y, x), (y, x))) # 추가 파라미터 스타트, 종료 추가
    visited[y][x] = True

    while q:
        y, x, (min_y, min_x), (max_y, max_x) = q.popleft()
        for dist in range(4):
            ny, nx = y + dy[dist], x + dx[dist]
            if 0 > ny or n <= ny or 0 > nx or n <= nx: continue
            if grid[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                # 행, 열 cnt
                #하나라도 현재 y, x 보다 크거나 작으면, 전부 해당 ny, nx 입력
                if x < nx or y < ny:
                    max_y, max_x = ny, nx
                    q.append((ny, nx, (min_y, min_x), (max_y, max_x)))
                elif x > nx or y > ny:
                    min_y, min_x = ny, nx
                    q.append((ny, nx, (min_y, min_x), (max_y, max_x)))

    # 좌표 값 구성 위해, + 1 로 정리하기
    return (max_y - min_y + 1, max_x - min_x + 1)


for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    # bfs?

    # 방문처리 필요 ->, 무리 갯수, 행 열 기록 필요
    grid_cnt = 0
    row_col_location = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and grid[y][x] != 0:
                visited[y][x] = True
                # bfs로 가지고 와야할게 행, 열 갯수 , (row, col) 으로 받아 정렬해서
                # (row, col) 으로 받아 보내야 함, 리스트로 변환 후 보내주기
                row_col_location.append(list(bfs(y, x, visited, grid, n)))

                #여기서 체크 되는게 행열 인접 하는 무리 갯수 리턴
                grid_cnt += 1

    # 1. 행열 곱의 정렬 / 2. 동일하면 행의 크기순으로 정렬
    # 키를 x로 임의 변수 지정(어떤 것으로든 설정 가능)
    # x : (1 조건, 2 조건) 으로 순차 정렬 하겠다 -> 3 조건 추가하려면 (x[0] * x[1], x[0], x[1] ) 이다
    # 1번 -> row * col 의 합 순으로 정렬,
    # 2번 -> 1번 값 동일하면 row 값 순으로 정렬
    row_col_location_sorted = sorted(row_col_location, key=lambda x: (x[0] * x[1], x[0]))

    print(f"#{tc} {grid_cnt}", end=" ")
    for y, x in row_col_location_sorted:
        print(y, x, end=" ")
    print()