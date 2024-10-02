from collections import deque

t = 10

def bfs(y, x, maze, visited):
    # 4방 탐색
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    q = deque()
    q.append((y, x))

    # 큐에 값이 있을때 까지 반복
    while q:
        y, x = q.popleft()
        # 4방향 돌면서 탐색

        # 이 경우는 도착지가 나오면 끝이기에 큐가 종료되어 
        # 큐를 꺼낸 상태에서 확인 불가이기에 이 코드는 틀린 것
        # if maze[y][x] == 3:
        #     return 1

        for i in range(4):
            # 내부 if 문 각 독립 순차 검사
            ny, nx = y + dy[i], x + dx[i]
            # 벽 통과 못하면 넘어가기
            if ny >= n or nx >= n or ny < 0 or nx < 0: continue

            # 만약 다음 지점에 해당값이 3이면
            # 종료 조건 설정, 큐에서 나온 좌표값이 3이면 도착지
            # 두 번째 조건 (첫 번째 조건과 무관하게 검사)
            if maze[ny][nx] == 3:
                # 1 리턴 후 함수 종료
                return 1

            # 종료 조건이 아니라면, 0이고, 방문처리 아닌 길로 다시 간다
            # 길로 가서 방문처리하고 앞으로 갈 길 큐에 넣어 넓히며 탐색
            # 세 번째 조건 (앞의 조건과 무관하게 검사)
            if maze[ny][nx] == 0 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

    # 도착지 없으면 0으로 리턴
    return 0


for tc in range(1, t+1):
    tc1 = int(input())
    n = 16

    maze = [list(map(int, input().strip())) for _ in range(n)]
    # 길 지나갔으면 다시 되돌아 오지 않게 처리 위한 배열
    visited = [[False]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            # 출발지 찾으면
            if maze[y][x] == 2 and not visited[y][x]:
                # 출발지 방문처리
                visited[y][x] =True
                result = bfs(y, x, maze, visited)

    print(f"#{tc} {result}")