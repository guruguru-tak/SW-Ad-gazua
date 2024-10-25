from collections import deque

def topology_Sort(graph, n, times):
    # 차수 0으로 초기화
    in_Degree = [0] * (n+1)
    # 최종 저장되는 누적 시간들
    result_Time = [0] * (n+1)
    # 큐 초기화, 다른 곳에서 지정시 들어온 겂 없어지고 또 초기화됨
    q = deque()

    # 각 노드의 차수를 계산
    for v in range(1, n+1):
        for e in graph[v]:
            in_Degree[e] += 1

    # 차수가 0인 노드들을 큐에 삽입하고 초기 시간을 설정
    for i in range(1, n+1):
        if in_Degree[i] == 0:
            q.append(i)
            result_Time[i] = times[i]

    # 큐로 돌리면서 차수 빼면서 선행 작업 수행
    # 위상 정렬 알고리즘을 사용해 최소 시간을 계산
    while q:
        v = q.popleft()

        for e in graph[v]:
            # 계속 -1 해서 차수 1로 들어오면
            in_Degree[e] -= 1
            # 누적 시간은, 작업 모두 한 가장 오래 걸린 시간
            result_Time[e] = max(result_Time[e],result_Time[v]+times[e])
            # 차수 0이면 큐에 넣어 작업 둘리기
            if in_Degree[e] == 0:
                q.append(e)

    return max(result_Time)


n = int(input())

graph = [[] for _ in range(n+1)]
# 걸리는 시간 저장 리스트
times = [0] * (n + 1)

for e in range(1, n+1):
    # 순서대로 1 ~ n 번 작업 정점에 엣지 들어온다
    time, op_cnt, *op_List  = list(map(int, input().split()))

    # 작업 시간
    times[e] = time

    for v in op_List:
        #  선행 관계에 있는 작업들의 번호 간선 연결
        graph[v].append(e)

result = topology_Sort(graph, n, times)
print(result)
