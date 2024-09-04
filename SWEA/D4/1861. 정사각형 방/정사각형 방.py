t = int(input())


def dfs(y, x):

    # 전역 선언
    global cnt
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 벽 조건이 아니면 +1 해서 재귀 다시 돌리기
        if 0 > nx or n <= nx or 0 > ny or n <= ny: continue
        # 다음 방이 현재 값의 방의 값에서 + 1 인지 조건문 확인 더이상 진행 불가하면 dfs 최종 값 메인으로 보내주기
        if rooms[ny][nx] == rooms[y][x] + 1:
            cnt += 1
            dfs(ny, nx)


for tc in range(1, t+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    #단방향이라 돌아갈 필요가 없고, 돌아갈 수 없어서 방문처리 리스트 불필요
    # 최대로 이동할 수 있는 방의 개수
    max_count = 0

    # 최대 이동 시작 방 번호
    start_room = 0

    for y in range(n):
        for x in range(n):
            # 현재 방에서 이동할 수 있는 방의 개수 -> 첫 방 입장 기본 디폴트 1칸 이동 한 것
            cnt = 1
            dfs(y, x)

            #dfs로 값 다 구했으니, 조건에 맞춰 최대 방 개수와 시작 방 번호를 갱신
            if cnt > max_count or (cnt == max_count and rooms[y][x] < start_room):
                max_count = cnt
                start_room = rooms[y][x]

    print(f"#{tc} {start_room} {max_count}")