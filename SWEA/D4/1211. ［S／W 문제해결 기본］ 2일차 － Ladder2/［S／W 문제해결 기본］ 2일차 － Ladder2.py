t = 10

for tc in range(1, t+1):
    _ = int(input())
    n = 100
    sadari = [list(map(int, input().split())) for _ in range(n)]


    # 시작점 해당 인덱스에 움직임 횟수 저장 한 후
    # 가장 큰수의 인덱스 출력
    idx_move = [0]*n

    # 스타트 x 지점 저장할 변수
    start_x = -1
    for x in range(n):
        # 0행부터 1 찾기
        if sadari[0][x] == 1:
            start_x = x

            # 첫 시작과 끝은 체크 안해도 되도록 짜서, 먼저 2 더해줌
            idx_move[x] += 2
            # 매 새로운 x 좌표마다 리셋
            visited = [[False] * n for _ in range(n)]
            visited[0][start_x] = True

            y = 1
            # y 가 -1 이 되면 마지막 0번지 행 돌아서 시작 지점으로 온 것
            while y < n - 2:

                # 시작 번지인 x 인덱스 값을 증가시킴
                idx_move[x] += 1
                # 매번 바뀐 값들 방문 처리 해주기
                visited[y][start_x] = True

                # 0과 1에 따라서 활동 나누기
                # 위로 올라가는 것보다 왼쪽 오른쪽 우선 활동

                # x좌표 0번지 벽이면 우, 하 만 가능
                if start_x == 0:
                    # 우 방향 1 이고, 방문 아니면 오른쪽 이동
                    if sadari[y][start_x + 1] == 1 and not visited[y][start_x + 1]:
                        start_x += 1
                    # 우 방향 0 이면
                    else:
                        # 방문 아니면 하 방향 내려가기
                        if sadari[y+1][start_x] == 1 and not visited[y+1][start_x]:
                            y += 1

                # x좌표 99번지 벽이면 좌, 하 만 가능
                elif start_x == n-1:
                    # 좌 방향 1 이고, 방문 아니면 왼쪽 이동
                    if sadari[y][start_x - 1] == 1 and not visited[y][start_x - 1]:
                        start_x -= 1
                    # 좌 방향 0 이면
                    else:
                        # 방문 아니면 하 방향 내려가기
                        if sadari[y + 1][start_x] == 1 and not visited[y + 1][start_x]:
                            y += 1

                # x 좌표 벽 아니면 좌, 우, 하 만 가능
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
                        # 결국 아래로 가야 함
                        # 왼쪽에서 넘어왔거나 오른쪽에서 넘어왔거나, 아래에서 넘어왔기에
                        # 방문처리 되어있어 뒤로 못가기 때문
                        elif sadari[y][start_x-1] == 0 or sadari[y][start_x+1] == 0:
                            # 방문 아니면 하 방향 내려가기
                            if sadari[y + 1][start_x] == 1 and not visited[y + 1][start_x]:
                                y += 1

    # 최단 거리 출력, 동일하면 가장 큰 x 좌표
    # min_num 은 idx_move에서 0보다 큰 조건의 값만 반복해서 찾음
    min_num = min(cnt for cnt in idx_move if cnt > 0)
    # 함수 enumerate: idx_move 리스트를 순회하면서 각 요소의 인덱스(idx)와 값(cnt)을 동시에 가져온다
    # max -> idx 기준으로 해서 동일하면 가장 큰 x 좌표 출력 됨
    result = max(idx for idx, cnt in enumerate(idx_move) if cnt == min_num)

    print(f"#{tc} {result}")