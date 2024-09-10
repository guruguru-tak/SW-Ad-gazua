t = 10
for tc in range(1, t+1):
    check_n = int(input())
    n = 8

    grid = [list(map(str, input().strip())) for _ in range(n)]

    str_line = []
    #일자로만 인정
    for y in range(n):
        for x in range(n):
            str_row = []
            str_col = []
            for c in range(check_n):
                if 0 <= x+c < n:
                    str_row.append(grid[y][x+c])
                    str_col.append(grid[x+c][y])
            if len(str_row) == check_n and len(str_col) == check_n:
                str_line.append(str_row)
                str_line.append(str_col)

    # 저장 리스트 인덱스 하나씩 회문체크
    result = 0
    for arr in str_line:
        cnt = 0
        for _ in range(check_n//2):
            if arr.pop(0) == arr.pop(-1):
                cnt += 1
            else:
                break

        #짝수 경우의 갯수
        if check_n % 2 == 0:
            if cnt == check_n/2:
                result += 1

        #홀수 경우의 갯수
        else:
            if cnt == check_n//2:
                result += 1

    print(f"#{tc} {result}")
