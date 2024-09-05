t = int(input())


def dfs(y, x):
    global cnt
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > ny or ny >= n or 0 > nx or nx >= n: continue
        #정확하게 들어온 y,x 의 값에서 정확히 1 더한게 next값고 같으면 cnt + 1,
        if (grid[y][x] + 1) == grid[ny][nx]:
            cnt += 1
            #넥스트 좌표에 재귀
            dfs(ny, nx)


for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_count = 0
    start_index = 0

    for y in range(n):
        for x in range(n):
            #한 칸을 띄운 후, 조건 있어 매 번 1로 초기화
            cnt = 1
            dfs(y, x)

            if cnt > max_count or (cnt == max_count and grid[y][x] < start_index):
                #최대 값을 max함수로 구하는게 아니라 그냥 가장 큰 것이면 값을 그대로 넣어 갱신
                start_index = grid[y][x]
                max_count = cnt

    print(f"#{tc} {start_index} {max_count}")
