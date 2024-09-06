import math

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    total_w = sum(arr)
    # depth: 현재 단계에서 선택(왼쪽/오른쪽) 해야하는 추의 인덱스
    # l_sum: 여태까지 왼쪽 추의 합
    # r_sum: 여태까지 오른쪽 추의 합


    def dfs(depth, l_sum, r_sum, remaining_sum):
        global result
        # 오른쪽 저울이 더 무거워지면 dfs 호출 중단
        if l_sum < r_sum:
            return

        # 모든 추를 다 배치한 경우
        if depth == N:
            result += 1
            return

        # 이거 가지치기만 추가하면 됩니다.
        if l_sum >= r_sum + remaining_sum:
            result += (2 ** (N-depth)) * math.factorial(N-depth)
            return


        # idx에 해당 추를 왼쪽에 놓는 경우
        # () 무슨 추를 놔야할까요 ?
        for i in range(N):
            if visited[i]: continue  # 방문한 적이 있으면 넘어간다 (순열에서 선택된 경우)
            visited[i] = True
            dfs(depth+1, l_sum + arr[i], r_sum , remaining_sum - arr[i])
            # 오른쪽에 놓는 경우
            dfs(depth+1, l_sum, r_sum + arr[i], remaining_sum - arr[i])
            visited[i] = False




    visited = [False] * N
    # 주어진 추를 하나씩 왼쪽에 올려놓고 시작
    # 왼쪽에 추를 하나 올려놨다고 치고! dfs 실행
    for i in range(N):
        """
        부분집합 => 해당 추를 왼쪽/오른쪽에 놓을거냐 선택
        파라미터 
        1. 재귀호출을 중단할 파라미터: 
        => 해당 추를 왼쪽/오른쪽에 놓을거냐 정해야하는 인덱스 (depth) => 
        => 종료조건 => 이 인덱스가 주어진 추의 개수에 도달하면 호출 중단
        2. DFS 누적해서 가져가고 싶은 값
        => 여태까지 왼쪽에 놓은 추들의 합, 여태까지 오른쪽에 놓은 추들의 합 
        """
        visited[i] = True  # i번째 추를 선택했다고 치니까, 방문 확인
        dfs(1, arr[i], 0, total_w - arr[i])
        visited[i] = False  # 원상 복구해줘야한다.

    print(f"#{test_case} {result}")