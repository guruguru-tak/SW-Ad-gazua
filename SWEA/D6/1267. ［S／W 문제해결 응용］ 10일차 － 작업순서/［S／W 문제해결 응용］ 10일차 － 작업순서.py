
from collections import deque

t = 10


def topology_Sort(graph, v_Size):
    # 먼저 시작인 0인지 아닌지 차수 구분 방문 배열 필요
    in_Degree = [0]*v_Size

    # 모든 노드 진입 작업차수 계산
    for u in range(1, v_Size):
        # 그래프에서 수 나눠서 받아주기
        for v in graph[u]:
            # 다른 노드로 들어오는 간선이 있을 때마다 해당 차수에 진입 차수를 증가
            in_Degree[v] += 1

    # print(in_Degree)

    # 진입차수 0인 노드 저장 큐 생성
    q = deque()

    for i in range(1, v_Size):
        if in_Degree[i] == 0:
            q.append(i)

    # 상 정렬된 결과를 저장해서 보낼 리스트
    result = []

    while q:
        # 진입 차수가 0인 노드를 큐에서 꺼냄
        u = q.popleft()

        # 모든 선행 작업이 완료된 상태
        # 선택된 노드를 결과 리스트에 보내기
        result.append(u)

        # 선택된 노드와 연결된 간선 제거
        for v in graph[u]:
            # 간선을 제거했으므로 진입 차수 -1 감소
            in_Degree[v] -= 1

            # 진입 차수가 0이 되면 큐에 추가
            # 새로운 작업 시작할 수 있는 루트 지정
            if in_Degree[v] == 0:
                q.append(v)

    # 결과 리스트의 크기가 노드의 수와 같으면 위상 정렬 성공
    if len(result) == v_Size-1:
        return result
    else:
        # 민약 모든 노드를 처리하지 못했다면 사이클이 존재하는 경우
        return []

for tc in range(1, t+1):
    v, e_Size = map(int, input().split())

    # 1부터 v 포함이기에 1 더해주기
    v_Size = v + 1

    line = list(map(int, input().split()))

    graph = [[] for _ in range(v_Size)]

    for i in range(0, len(line)-1, 2):
        v, e = i, i+1
        graph[line[v]].append(line[e])

    # print(graph)
    # 위상정렬 , 출력 값 담아서 보내기
    result = topology_Sort(graph, v_Size)

    print(f"#{tc}", *result)