from collections import deque

def bfs(n, m, grid):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    time = 0

    #이 루프는 빙산이 두 덩어리로 분리되거나 완전히 녹아 없어질 때까지 계속해서 반복
    #루프 내에서 빙산을 녹이고, 덩어리 수를 체크하며 종료 조건을 확인
    while True:
        # 빙산 녹이기 로직 부분
        #new_Grid는 새롭게 녹은 빙산의 상태를 저장하는 그리드
        #현재 상태에서 주변 바다와 맞닿은 면적만큼 빙산을 녹인 후의 상태를 나타냄
        new_Grid = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    water_count = 0
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                            #만약 인접한 셀이 바다라면 water_count를 증가시켜 해당 빙산의 높이를 그만큼 줄임
                            water_count += 1
                    #빙산의 높이가 음수가 되지 않도록 한다. 항상 0이랑 최대값 비교
                    new_Grid[i][j] = max(0, grid[i][j] - water_count)

        #기존의 grid를 새로 녹인 new_Grid로 업데이트
        grid = new_Grid
        #빙산이 한 번 녹을 때마다 시간이 1 증가, 빙산이 녹는 과정을 반복할 때마다 증가
        time += 1

        # BFS로 덩어리 수 세기 로직
        visited = [[False] * m for _ in range(n)]
        #현재 빙산 덩어리의 수를 세는 변수
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visited[i][j]:
                    count += 1
                    #count가 2 이상이 되면 빙산이 분리된 것이므로,
                    # 현재 시간을 출력하고 함수를 종료
                    if count > 1:
                        #빙산 최초 분리 시간 입력
                        print(time)
                        ##함수의 실행을 종료, return이 호출되면 그 아래의 코드는 더 이상 실행되지 않음
                        return

                    #튜플 개별요소 아닌 묶어서 q에 저장
                    q = deque([(i, j)])
                    visited[i][j] = True

                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and not visited[nx][ny]:
                                #큐에서 좌표를 하나씩 꺼내서 상하좌우 네 방향으로 인접한 빙산 부분을 탐색
                                #인접한 빙산이 아직 방문되지 않았고, 바다가 아닌 경우 그 좌표를 큐에 추가하고 방문 처리
                                visited[nx][ny] = True
                                q.append((nx, ny))

        #빙산이 모두 녹아서 아무것도 없을 때
        #전체 그리드를 탐색한 후 빙산 덩어리가 하나도 남아 있지 않은 경우를 처리
        #빙산이 모두 녹아 없어졌다면, count가 0이 되므로 0을 출력하고 함수를 종료
        if count == 0:
            print(0)
            #함수의 실행을 종료, return이 호출되면 그 아래의 코드는 더 이상 실행되지 않음
            return


n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

bfs(n, m, grid)

