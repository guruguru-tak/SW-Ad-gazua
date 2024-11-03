import sys
# sys.stdin = open("input.txt", "r", encoding='utf-8')

from collections import deque
t = int(input())


def topology_sort(last_Building_Num, graph, time_Graph, building_Cnt):
    # 차수 초기화
    in_Degree = [0] * (building_Cnt + 1)


    # 각 노드의 차수를 계산
    for v in range(1, building_Cnt+1):
        for e in graph[v]:
            in_Degree[e] += 1

    # 각 넘어가는 지점마다 시간 더해서 해당 위치 배열에 시간 저장장
    result_Time = [0] * (building_Cnt + 1)
    q = deque()

    # 차수가 0인 노드들을 큐에 삽입하고 초기 시간을 설정
    for i in range(1, building_Cnt+1):
        if in_Degree[i] == 0:
            q.append(i)
            # 시작지점 시간 더하기
            result_Time[i] += time_Graph[i]

    # 큐로 돌리면서 차수 빼면서 선행 작업 수행
    # 위상 정렬 알고리즘을 사용해 건설 시간을 계산
    while q:
        v = q.popleft()

        for e in graph[v]:
            # 계속 -1 해서 차수 1로 들어오면
            in_Degree[e] -= 1
            # 더해줄 건설 완료 최장 시간 담아주기
            # 현재 건물의 완료 시간 이후에 후속 건물의 건설이 시작되므로, 최대 시간을 기록

            # result_Time[e] => 제일 먼저 들어오는 e 결과 시간
            # result_Time[v] + time_Graph[e] => 차수 줄어들 때 전에 해당하는 정점의 시간 + 현재 간선 걸리는 시간
            # 두 개 중 최대값으로 한 번만 걸리는 최대값을 result_Time[e] 저장 후 차수 줄어들면 이 값이 result_Time[v] 값 됨
            result_Time[e] = max(result_Time[e], result_Time[v] + time_Graph[e])

            # 차수가 0이면 모든 건물 건설 완료
            if in_Degree[e] == 0:
                # 마지막 시간 했으면 다시 큐에 넣어 다음 작업 진행
                q.append(e)

    # 목표 건물의 건설 시간을 반환
    return result_Time[last_Building_Num]


for tc in range(t):

    building_Cnt, orderRule_Cnt = map(int, input().split())

    time_Graph = [-1] * (building_Cnt+1)
    graph = [[] for _ in range((building_Cnt+1))]

    line = list(map(int, input().split()))

    for _ in range(orderRule_Cnt):
        v, e = map(int, input().split())
        graph[v].append(e)

    last_Building_Num = int(input())

    for i in range(1, building_Cnt+1):
        time_Graph[i] = (line[i-1])

    result = topology_sort(last_Building_Num, graph, time_Graph, building_Cnt)

    print(result)