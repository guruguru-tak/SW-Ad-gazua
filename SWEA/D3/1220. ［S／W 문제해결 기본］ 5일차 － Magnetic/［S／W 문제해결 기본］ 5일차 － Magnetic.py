t = 10
for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    #1은 N극 2는 S극
    # 위는 N극, 밑은 S극
    # 서로 맞다으면 자성 연결

    #맞닿은 것 걧수 카운트 변수
    cnt = 0
    for x in range(n):
        for y in range(n):
            #col 만 움직임, N 극 선택이면
            if grid[y][x] == 1:
                #본인 위치 1 제거 위해 1부터 인덱스 시작
                for c in range(1, n):
                    #벽세우기
                    if 0 <= y+c < n:
                        #1 바로 다음 2만나면 카운트 세기
                        #break 걸면 현재 돌고 있는 c 부분 for 문 종료
                        #외부 y for문 작동한다
                        #맨처음 0, 0 에서 y가 0인 경우 break
                        if grid[y+c][x] == 2:
                            cnt += 1
                            break
                        #만약 바로 다음에 0이나 1이 있으면 바로 정지
                        elif grid[y+c][x] == 1:
                            break
                        #다음 칸 0이면 다음 진행 위해 pass
                        elif grid[y+c][x] == 0:
                            pass
            # 0이나 2면 패스
            else:
                pass

    print(f"#{tc} {cnt}")
