t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    selected_jobs = list(map(int, input().split()))

    time = list(map(int, input().split()))

    # 각 작업에 대해 최대 설득 비용을 저장할 배열
    max_k_list = [0] * k
    cost_list = []

    # 모든 작업 순회
    for i in range(n):
        job_index = selected_jobs[i]
        cost = time[i]

        # 현재 작업 번호에 대해 최대 설득 비용 확인
        if max_k_list[job_index-1] <= cost: # 기존 비용보다 크거나 같으면 갱신
            if max_k_list[job_index-1] > 0: # 기존 값이 0보다 크다면, 비용 리스트에 추가
                cost_list.append(max_k_list[job_index-1])
            max_k_list[job_index-1] = cost # 최대 비용 갱신
        else:
            # 기존 비용이 더 크면 그대로 비용 리스트에 추가
            cost_list.append(cost)

    # 선택되지 않은 작업의 개수 계산
    num_unselected = 0
    for max_k in max_k_list:
        if max_k == 0:
            num_unselected += 1

    # 일이 더많으면 일해야 함
    # 설득 시간은 일이 많을수록 증가하므로, 일이 많이 걸리는 사람부터 설득하여 균등하게 분배
    # 설득의 최소화를 위해 작업 시간을 기준으로 정렬 후, 가중치가 큰 작업부터 분배를 고려

    # 최소 시간 합 -> 정렬 가중치 큰 수
    # 설득 비용을 정렬 -> 오름차순
    cost_list.sort()

    # 최소 비용 합산
    result = 0
    for i in range(num_unselected):
        result += cost_list[i]

    print(f"#{tc} {result}")