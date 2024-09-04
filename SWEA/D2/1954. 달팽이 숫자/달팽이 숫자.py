t = int(input())
for tc in range(1, t +1):

    n = int(input())

    grid = [[0]*n for _ in range(n)]
    #4방 순서대로 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    dist = 0
    nx, ny = 0, 0


    #입력 증가 값
    for i in range(1, n*n+1):
        #조건, 0이 아니면 숫자 넣고 아니면 돌아라 -> 방향 조절 필요
        #넣을 데이터 모든 배열 돌 때까지 증가


        grid[ny][nx] = i
        nx += dx[dist]
        ny += dy[dist]

        #벽 도착이거나, 0이 아닌 수 만나면 dx, dy 방향 전환
        if ny < 0 or nx < 0 or nx >= n or ny >= n or grid[ny][nx] != 0:
            #방향 전환한 채로 입력된 next   값 제거해주기
            nx -= dx[dist]
            ny -= dy[dist]
            #dist 방향전환 수식 필요
            # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
            dist = (dist+1) % 4
            #변경된 dist로 진행
            nx += dx[dist]
            ny += dy[dist]
    print(f"#{tc}")
    for row in grid:
        print(*row)
    print(end="")