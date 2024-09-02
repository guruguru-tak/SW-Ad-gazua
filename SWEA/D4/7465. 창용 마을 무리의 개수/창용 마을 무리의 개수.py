from collections import deque
t = int(input())


def bfs(i, adj_list, visited, n_top):
    q = deque()
    q.append(i)
    visited[i] = True

    while q:
        v = q.popleft()
        for g in range(len(adj_list[v])):
            if not visited[adj_list[v][g]]:
                visited[adj_list[v][g]] = True
                q.append(adj_list[v][g])

for tc in range(1, t + 1):
    n_top, m_node = map(int, input().split())

    adj_list = [[] for _ in range(n_top+1)]
    visited = [False] * (n_top+1)


    #그래프 입력 구성
    for _ in range(m_node):
        x, y = map(int, input().split())
        #방향 그래프일 경우 한 줄만
        adj_list[x].append(y)
        #무방향이라면 양 방향도 들어와야 한다
        adj_list[y].append(x)

    result = 0
    for i in range(1, n_top+1):
        if not visited[i]:
            result += 1
            bfs(i, adj_list, visited, n_top)


    print(f"#{tc} {result}")