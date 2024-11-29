
from collections import deque
from itertools import product
# 중복 순열 - 한 번 선택한 요소를 다시 선택 가능
# 순서가 다르면 다른 경우로 간주
# [A,A],[A,B],[B,A],[B,B]

t = int(input())

# 해당 열(grid_x)에서 가장 위에 있는 벽돌의 위치를 반환.
# 벽돌이 없으면 None을 반환.
def find_first_brick(grid, grid_x):
    h = len(grid)
    # 위에서부터 탐색
    for grid_y in range(h):
        # 벽돌이 있는 위치를 찾음
        if grid[grid_y][grid_x] > 0:
            return grid_y
    # 벽돌이 없는 경우
    return None

# 구슬을 떨어뜨려 벽돌 제거를 시뮬레이션 함수
def drop_ball(grid, grid_x):
    # y축 길이
    h = len(grid)
    # x 축 길이
    w = len(grid[0])

    # 깊은 복사로 시뮬할 그리드 생성
    new_copy_grid = [x[:] for x in grid]

    # 공이 닿는 첫번째 벽돌 찾기
    # 해당 열(x)에서 가장 위에 있는 벽돌 찾기
    first_grid_y = find_first_brick(new_copy_grid, grid_x)
    if first_grid_y is None:
        # 벽돌이 없으면 그대로 반환
        return new_copy_grid

    # bfs 로 네트워크 처럼 퍼지듯이 벽돌 제거
    q = deque()
    q.append((first_grid_y, grid_x, new_copy_grid[first_grid_y][grid_x]))
    # 첫 번째 벽돌 제거
    new_copy_grid[first_grid_y][grid_x] = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        y, x, pow = q.popleft()

        for i in range(4):
            for p in range(1, pow):
                # 본인 블럭 포함 pow까지라 범위는 1 <= < pow
                ny = (dy[i]*p) + y
                nx = (dx[i]*p) + x
                if 0 <= ny < h and 0 <= nx < w and new_copy_grid[ny][nx] > 0:
                    # 앞으로 퍼질 ny, nx 값과 다음 pow 값 큐에 넣기
                    q.append((ny, nx, new_copy_grid[ny][nx]))
                    # 터지면 0으로 바꿔주기
                    new_copy_grid[ny][nx] = 0

    # 가장 아래까지 내려가야 하기에 아래 -> 위로 탐색
    # x 축 한개 독립적 하강
    for x in range(w):
        # 아래쪽부터 채우기 시작
        fill_y = h - 1
        # 초기값은 맨 아래 행의 인덱스(h-1)
        # 맨 아래 행부터 위로 탐색 for 문 반복
        for y in range(h - 1, -1, -1):
            # 현재 셀이 0보다 크면 벽돌 존재 -> 벽돌을 아래로 이동
            # 현재 셀 0이면 벽돌 없음 fill_y h-1, y h-2 로 간다
            if new_copy_grid[y][x] > 0:
                # bfs 이용해서 이미 0처리 된 후 벽돌 한개라도 발견시
                # new_copy_grid[y][x] -> new_copy_grid[fill_y][x] 넣기
                new_copy_grid[fill_y][x] = new_copy_grid[y][x]

                # 만약 fill_y != y 다른위치여야 작동
                # 만약 현재 넣을 fill_y 가 y 위치 이동 후 원래 y 는 0
                if fill_y != y:
                    new_copy_grid[y][x] = 0
                # 벽돌을 채운 후, fill_y를 1 감소하여 다음 빈 칸으로 이동
                fill_y -= 1

    return new_copy_grid


# 깊은 복사 한 그리드 남은 벽돌 갯수 세는 함수
def count_remain_bricks(h, w, temp_grid):
    count = 0
    for y in range(h):
        for x in range(w):
            # 해당 값이 0이상이면 벽돌 존재
            if temp_grid[y][x] > 0:
                count += 1
    return count

# 벽돌 깨는 메인 함수
def solve_bricks(n, w, h, grid):
    # 최소 남은 블록 구하기 위해 최대값 설정
    min_remain = 10**18
    
    
    # 한 열에 3번 구슬 떨어뜨릴 수 있고, 열마다 순서를 다르게 떨어뜨릴 수 있다
    # (9, 9, 9) -> 모두 9번지 열에 떨어뜨리기
    # (1, 2, 3), (3, 2, 1) -> 순서 다르게 터지는것 기록해서 비교
    # (1, 2, 2) (1, 1, 1) -> 중복도 허용해야 모두 구해 최소값 구함
    # 모든 가능한 구슬 투하 조합 사용(중복순열, product)
    
    # range(w) -> 구슬 떨어뜨릴 수 있는 열의 번호
    # repeat = n -> 구슬을 n번 떨어뜨릴 경우, 모든 경우의 조합을 생성
    for drops in product(range(w), repeat=n):
        # 똑같이 바꿀 그리드 깊은 복사 생성
        temp_grid = [x[:] for x in grid]
        # print(drops)

        # 각 열(x축) 에 대해 구슬 투하
        for grid_x in drops:
            temp_grid = drop_ball(temp_grid, grid_x)

        remain = count_remain_bricks(h, w, temp_grid)
        min_remain = min(min_remain, remain)

        # print(f"Drops: {drops}, Remaining bricks: {remain}")
    return min_remain

for tc in range(1, t+1):
    # 구슬 던지는 횟수, 박스 넓이, 높이
    n, w, h = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(h)]

    result = solve_bricks(n, w, h, grid)

    print(f"#{tc} {result}")
