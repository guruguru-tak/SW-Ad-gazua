
from collections import deque

#벽의 값 있어야 해서, n도 인자 추가
def bfs(x, y, n, grid, visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    #(x, y) 묶어서 인자 추가
    q.append((x, y))
    visited[x][y] = True
    #지정된 해당 1번 count 계산
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #벽 세우기
            if 0 <= nx < n and 0 <= ny < n:
                #그리드 해당값 방문처리
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # (nx, ny) 묶어서 인자 추가
                    q.append((nx, ny))
                    count += 1
    return count


n = int(input())

grid = [list(map(int, input().strip())) for _ in range(n)]
#그리드 배열 방문처리 배열 만들기
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            # BFS 함수가 반환한 단지 크기를 result 리스트에 추가
            # 리스트에 추가되는 값은 단지의 크기
            result.append(bfs(i, j, n, grid, visited))

#단지 오름차순 정렬
result.sort()

#총 단지수 result 저장 길이 먼저 출력
print(len(result))
# print(result)
for count in result:
    #해당단지, append 된 result 리스트 각 인자를 출력
    print(count)

