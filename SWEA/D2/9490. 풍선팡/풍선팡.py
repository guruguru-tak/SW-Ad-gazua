t = int(input())

for tc in range(1, t+1):
    grid_y, grid_x = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(grid_y)]

    # 최대값 구하기
    result = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for y in range(grid_y):
        for x in range(grid_x):
            # 퍼질 값
            spread = grid[y][x]
            count = 0

            # 본인 위치 값 먼저 더하기
            count += grid[y][x]
            for i in range(4):
                # 퍼지는 범위 0이 아닌 1부터 spread 까지 (< spread+1)
                for r in range(1, spread+1):
                    ny = dy[i]*r + y
                    nx = dx[i]*r + x

                    if 0<=ny<grid_y and 0<=nx<grid_x:
                        count += grid[ny][nx]
            # print(count)
            result = max(result, count)

    print(f"#{tc} {result}")