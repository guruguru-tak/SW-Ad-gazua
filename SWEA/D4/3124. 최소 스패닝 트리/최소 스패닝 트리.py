from heapq import heappop, heappush

# 최소 스패닝 트리 -> prim(heap) 사용
t = int(input())


def prim_mst(v, graph):
    # 방문 처리
    visited = [False] * (v+1)

    # 우선순위 큐, 빈 리스트 만들기
    pq = []
    # heap -> 가중치 비교값 제일 앞으로 보내야 함
    # (가중치, 시작 노드), 임의의 노드 1번에서 시작
    heappush(pq, (0, 1))

    total_cost = 0

    # 모든 노드가 다 들어가는지 체크 변수
    edges_used = 0

    while pq:
        cost, node = heappop(pq)

        # 방문한 노드면 넘어가게
        if visited[node]:
            continue

        # 아니라면 방문 처리후
        visited[node] = True
        # 가중치를 전체 값에 더해주고
        total_cost += cost

        # 간선 사용 횟수 +1
        edges_used += 1
        # 모든 노드가 연결되었으면 종료
        if edges_used == v:
            break

        # 현재 노드와 연결된 모든 간선을 탐색
        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heappush(pq, (next_cost, next_node))

    # 입력으로 주어지는 그래프는 하나의 연결 그래프임이 보장된다.
    # 보장 안되면 -> if edges_used == v else -1 => 출력 return 필요
    return total_cost

for tc in range(1, t+1):

    # 합이 최소 1,000,000을 넘지 않는다
    min_result = 10**18
    v, e = map(int, input().split())

    # 그래프 간선 입력/ 인접 리스트
    graph = [[] for _ in range(v+1)]

    # 간선 반복 입력
    for _ in range(e):
        a, b, c = map(int, input().split())

        # 가중치 있는 c 가 항상 앞에 와야 한다
        # a에서 b로 가는 비용 c
        graph[a].append((c,b))
        # b에서 a로 가는 비용 c (무향 그래프)
        graph[b].append((c,a))

    # prim 알고리즘 사용
    result = prim_mst(v, graph)

    print(f"#{tc} {result}")
