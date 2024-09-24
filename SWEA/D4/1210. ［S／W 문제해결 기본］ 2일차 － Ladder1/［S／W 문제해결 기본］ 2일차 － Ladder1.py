t = 10

for tc in range(1, t+1):
    _ = int(input())
    n = 100
    sadari = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    # 스타트 x 지점 저장할 변수
    start_x = -1
    for x in range(n):
        # 마지막 99행에서 2 찾기
        if sadari[n-1][x] == 2:
            start_x = x
            visited[n-1][start_x] = True

    # y 행 98부터 시작
    y = 98
    # y 가 -1 이 되면 마지막 0번지 행 돌아서 시작 지점으로 온 것
    while y != 0:
        # 매번 바뀐 값들 방문 처리 해주기
        visited[y][start_x] = True

        # 0과 1에 따라서 활동 나누기
        # 위로 올라가는 것보다 왼쪽 오른쪽 우선 활동

        # x좌표 0번지 벽이면 우, 상 만 가능
        if start_x == 0:
            # 우 방향 1 이고, 방문 아니면 오른쪽 이동
            if sadari[y][start_x + 1] == 1 and not visited[y][start_x + 1]:
                start_x += 1
            # 우 방향 0 이면
            else:
                # 방문 아니면 상 방향 올라가기
                if sadari[y-1][start_x] == 1 and not visited[y-1][start_x]:
                    y -= 1

        # x좌표 99번지 벽이면 좌, 상 만 가능
        elif start_x == n-1:
            # 좌 방향 1 이고, 방문 아니면 왼쪽 이동
            if sadari[y][start_x - 1] == 1 and not visited[y][start_x - 1]:
                start_x -= 1
            # 좌 방향 0 이면
            else:
                # 방문 아니면 상 방향 올라가고
                if sadari[y - 1][start_x] == 1 and not visited[y - 1][start_x]:
                    y -= 1

        # x 좌표 벽 아니면 좌, 우, 상 만 가능
        else:
            # x좌표 범위
            if 0 <= start_x <= n:
                # 한 번 지나간 자리는 다시 가면 안되기에 방문처리 확인 필요,
                # 좌, 우 1이고 방문 아니면
                if (sadari[y][start_x-1] == 1 and not visited[y][start_x-1]) or (sadari[y][start_x+1] == 1 and not visited[y][start_x+1]):
                    # 좌 1 이고, 방문 아니면 왼쪽 이동
                    if sadari[y][start_x-1] == 1 and not visited[y][start_x-1]:
                        start_x -= 1
                    # 우 1 이고, 방문 아니면 오른쪽 이동
                    elif sadari[y][start_x+1] == 1 and not visited[y][start_x+1]:
                        start_x += 1
                # 좌, 우 둘 중에 아무거나 0이면
                # 결국 위로 가야 함
                # 왼쪽에서 넘어왔거나 오른쪽에서 넘어왔거나, 아래에서 넘어왔기에
                # 방문처리 되어있어 뒤로 못가기 때문
                elif sadari[y][start_x-1] == 0 or sadari[y][start_x+1] == 0:
                    # 위로 올라가기
                    if sadari[y-1][start_x] == 1 and not visited[y-1][start_x]:
                        y -= 1

    print(f"#{tc} {start_x}")