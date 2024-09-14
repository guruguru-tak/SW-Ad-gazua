t = 10
for tc in range(1, t+1):
    _ = input()
    n = 100
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0

    #행의 합, 열의 합 구하기
    for y in range(n):
        sum_Cross1 = 0
        sum_Cross2 = 0
        sum_Row = 0
        sum_Col = 0
        for x in range(n):
            # 행끼리 합
            sum_Row += grid[y][x]
            # 열끼리 합
            sum_Col += grid[x][y]
            # 정방향 대각선 합
            sum_Cross1 += grid[x][x]
            # 역방향 대각선 합
            sum_Cross2 += grid[n-x-1][x]

        # 전체 합의 최대값 비교
        # max_sum 함께 비교 안하면 가장 나중에 나온 최대값을 반영
        max_sum = max(max_sum, sum_Row, sum_Col, sum_Cross1, sum_Cross2)

    print(f"#{tc} {max_sum}")