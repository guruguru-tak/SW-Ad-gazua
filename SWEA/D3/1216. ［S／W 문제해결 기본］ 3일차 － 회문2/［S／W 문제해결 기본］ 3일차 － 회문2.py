t = 10
for tc in range(1, t+1):
    # 테케 번호 무작위로 주기에 tc로 뽑으면 오류 남
    testcase = int(input())
    n = 100
    grid = [list(input().strip()) for _ in range(n)]

    # 최대 길이 찾기
    max_Result =0

    # 홀수 기준 최대길이 먼저 찾기
    for y in range(n):
        for x in range(n):
            # 기본 자기 위치 1
            cnt_row = 1
            cnt_col = 1
            # 회문 인덱스 2배씩 증가기에 전체 길이의 // 2 가 범위
            for r in range(1, n//2):
                # 벽세우기
                if x - r < 0 or x + r >= n: continue
                # 행
                # 현재 인덱스 기준 좌, 우 계속 + 1 씩 해서 비교
                if grid[y][x+r] == grid[y][x-r]:
                    cnt_row += 2
                else:
                    break
            for r in range(1, n//2):
                if x - r < 0 or x + r >= n: continue
                # 열
                if grid[x+r][y] == grid[x-r][y]:
                    cnt_col += 2
                else:
                    break
            # 최대값 비교
            max_Result = max(max_Result, cnt_row, cnt_col)

        # 짝수 기준 최대길이 찾기
        for y in range(n):
            for x in range(n):
                # 기본 자기 위치 0
                cnt_row = 0
                cnt_col = 0
                # 회문 인덱스 2배씩 증가기에 전체 길이의 // 2 가 범위
                for r in range(1, n // 2):
                    if x - r + 1< 0 or x + r >= n: continue
                    # 행
                    # 현재 인덱스와 1칸 바로 옆에 2개씩 비교
                    if grid[y][x + r] == grid[y][x - r + 1]:
                        cnt_row += 2
                    else:
                        break
                for r in range(1, n // 2):
                    if x - r  + 1< 0 or x + r >= n: continue
                    # 열
                    if grid[x + r][y] == grid[x - r + 1][y]:
                        cnt_col += 2
                    else:
                        break
                max_Result = max(max_Result, cnt_row, cnt_col)


    print(f"#{testcase} {max_Result}")