import sys
import heapq

# sys.stdin = open("input.txt", "r", encoding='utf-8')

input = sys.stdin.readline

n, m, k, x = map(int, input().strip().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 도로 정보 입력
for _ in range(m):
    v, e = map(int, input().strip().split())
    # 가중치가 1인 도로로 연결 -> 나중에 도시 지날 때마다 이 가중치 추가하여 cost가 됨
    # 이 최소 cost 값이 distance[index] 에 할당
    graph[v].append((e, 1))

# 최단 거리위해 무한대 리스트 초기화
distance = [10**18]*(n+1)
# 출발 도시의 거리는 0
distance[x] = 0

# 다익스트라 알고리즘을 위한 우선순위 큐(Priority Queue)
# 우선적으로 더 짧은 거리부터 처리
pq = []
                # (거리, 도시)
heapq.heappush(pq, (0, x))

while pq:
    # 우선순위 큐(pq)에서 가장 작은 값을 꺼내는 부분
    # 우선순위 큐는 최소 힙으로 구현되어 있기 때문에,
    # 항상 가장 작은 값이 우선적으로 나온다
    # 초기상태 urrent_dist = 0, current_node = 1
    # 현재 도시 1에서 출발하여 연결된 다른 도시로 가는 경로를 탐색
    current_dist, current_node = heapq.heappop(pq)

    # 이미 처리된 노드라면 무시
    # 현재 노드(current_node)에 대해 이미 더 짧은 거리로 처리한 적이 있는지 확인하는 부분
    if distance[current_node] < current_dist:
        continue

    # 인접 노드 확인
    for next_node, weight in graph[current_node]:
        # cost는 현재 노드까지의 거리(current_dist) + 현재 노드에서 인접 노드로 가는 거리(weight)로 계산
        cost = current_dist + weight

        # 더 짧은 경로가 발견되면 업데이트
        # (distance[next_node])보다 짧다면, 더 짧은 경로가 발견되었다는 뜻
        if cost < distance[next_node]:
            # 새로운 최단 거리를 기록
            distance[next_node] = cost
            # 새로 발견된 더 짧은 경로를 우선순위 큐에 추가
            # 이를 통해 다음 번에는 이 더 짧은 경로를 먼저 처리
            heapq.heappush(pq, (cost, next_node))


result = []
# i 는 도시 번호
for i in range(1, n+1):
    # k만큼 떨어진 도시를 찾기
    if distance[i] == k:
        result.append(i)

if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)
