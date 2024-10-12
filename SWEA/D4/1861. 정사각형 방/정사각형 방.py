t = int(input())


def dfs(y, x, cnt):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue

        # 인접 방이 정확히 1차이 나는지 비교
        if grid[ny][nx] == grid[y][x] + 1:
            # 1차이 나면 현재값 cnt 할당후 재귀
            cnt = dfs(ny, nx, cnt+1)
    # 차이나는 것 없으면 종료
    return cnt


for tc in range(1,t +1):
    n = int(input())

    grid = [list(map(int, input().split())) for _ in range(n)]

    # 최소 방 번호
    min_Room_Num = 10**18

    # cnt 움직일 횟수
    max_Cnt = 0


    for y in range(n):
        for x in range(n):

            # - 1 씩 차이기에 방문처리 필요없음
            room_Num = grid[y][x]
            # 현재 위치에서 DFS 탐색
            cnt = dfs(y, x, 1)
            # 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것
            # cnt 가 max보다 크면 갱신
            if cnt > max_Cnt:
                max_Cnt = cnt
                min_Room_Num = room_Num
            # max와 cnt 같으면 가장 작은 방 번호 보내주기
            elif cnt == max_Cnt and room_Num < min_Room_Num:
                min_Room_Num = room_Num

    print(f"#{tc} {min_Room_Num} {max_Cnt}")