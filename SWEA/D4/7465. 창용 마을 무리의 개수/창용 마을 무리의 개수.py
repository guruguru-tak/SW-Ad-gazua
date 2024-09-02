from collections import deque
t = int(input())


def bfs(i, adj_list, visited):
    q = deque()
    #넘어온 i 인덱스 값을 먼저 확인 후 방문처리
    q.append(i)
    visited[i] is True

    #큐가 빌 때까지 반복
    while q:
        #현재 넣은 값 v로 꺼내서
        v = q.popleft()
        # v 번 인덱스 해당하는 인접리스트 안에 값 전부 참조
        for g in range(len(adj_list[v])):
            #방문처리 안되어 있으면
            if visited[adj_list[v][g]] is False:
                #방문처리하고
                visited[adj_list[v][g]] = True
                #큐에 넣기
                q.append(adj_list[v][g])

for tc in range(1, t + 1):
    n_top, m_node = map(int, input().split())


    adj_list = [[] for _ in range(n_top+1)]
    visited = [False] * (n_top+1)


    #그래프 입력 구성
    for _ in range(m_node):
        line = list(map(int, input().split()))
        # 연결 없이 관계없는 정점 제거
        if len(line) > 1:
            v, g = line
            #방향 그래프일 경우 한 줄만
            adj_list[v].append(g)
            #무방향이라면 양 방향도 들어와야 한다
            adj_list[g].append(v)

    result = 0
    for i in range(1, n_top+1):
        #방문하지 않으면
        if visited[i] is False:
            #무리 갯수 추가 후
            result += 1
            #bfs 호출
            bfs(i, adj_list, visited)


    print(f"#{tc} {result}")