t = 10
for tc in range(1, t+1):
    repeat_Cnt = int(input())
    n = 8
    grid = [list(input().strip()) for _ in range(8)]


    result = 0
    # 로우 계산
    for y in range(n):
        for x in range(n):
            # x 변경 시마다 cnt 리셋
            cnt_Row = 0
            # 회문 범위는 반복문의 몫만큼
            for r in range(repeat_Cnt//2):
                # 회문 길이 벽
                if (x+repeat_Cnt-1)-r < n:
                    # 회문 첫 번째 -> x + r
                    # 회문 마지막 -> x+repeat_Cnt-1)-r
                    # r 의 증가로 회문 좌우 인접 비교하게 됨
                    if grid[y][x+r] == grid[y][(x+repeat_Cnt-1)-r]:
                        cnt_Row += 2
                    else:
                        break
            # 회문 길이 홀수, 짝수에 따라 수식 달리 한다
            if repeat_Cnt % 2 == 0:
                if cnt_Row == repeat_Cnt:
                    result += 1
            else:
                if cnt_Row + 1 == repeat_Cnt:
                    result += 1

    # 컬럼 계산
    for x in range(n):
        for y in range(n):
            # x 변경 시마다 cnt 리셋
            cnt_Col = 0
            for r in range(repeat_Cnt//2):
                if (y+repeat_Cnt-1)-r < n:
                    if grid[y+r][x] == grid[(y+repeat_Cnt-1)-r][x]:
                        cnt_Col += 2
                    else:
                        break

            if repeat_Cnt % 2 == 0:
                if cnt_Col == repeat_Cnt:
                    result += 1
            else:
                if cnt_Col + 1 == repeat_Cnt:
                    result += 1

    print(f"#{tc} {result}")
