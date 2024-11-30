from collections import deque

t = int(input())

def bfs(n, graph):
    # 방문 여부
    visited = [False]*(n+1)

    q = deque()

    # (상원이 번호, bfs 퍼지는 깊이)
    q.append((1, 0))

    # 상원이 방문처리
    visited[1] = True

    # 초대장 갯수
    count = 0

    while q:
        node, depth = q.popleft()

        # 깊이가 2 초과인 경우의 친구는 초대하지 않음
        # 다른 친구 검색해야 해서 break 아님
        # 상원이(0) -> 친한친구(1) -> 친한친구(2)
        # 상원이가 시작 -> 깊이 레벨 2 -> 0부터 2까지임
        # 다만 앞서 1레벨에서 2레벨로 초대장 이미 카운트 해서 2레벨 초과시 컨티뉴
        if depth >= 2:
            continue

        # 1레벨에서 깊이 증가하면서 2레벨 친구 초대장 증가
        # 연결된 친구 검색
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                # 초대장 증가(다음 노드인 사람의 친구에게)
                count += 1
                # 레벨 증가
                q.append((next_node, depth+1))

    return count

for tc in range(1, t+1):
    # 반 n 명(1~N),
    n, m = map(int, input().split())

    # 1번 학생 상원 -> 힙에 0, 1부터 시작
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        # a번 학생과 b번 학생이 서로 친한 친구 관계
        a, b = map(int, input().split())

        # 양방향으로 탐색 필요
        graph[a].append(b)
        graph[b].append(a)

    # BFS로 초대할 학생 수 계산
    result = bfs(n, graph)

    print(f"#{tc} {result}")
