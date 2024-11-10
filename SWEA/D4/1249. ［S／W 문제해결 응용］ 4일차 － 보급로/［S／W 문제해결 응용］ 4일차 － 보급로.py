import heapq

def min_recovery_cost(grid):
    n = len(grid)
    # 복구 비용을 저장할 2D 배열, 큰 값으로 초기화
    recovery_cost = [[float('inf')] * n for _ in range(n)]
    recovery_cost[0][0] = 0  # 시작점의 비용을 0으로 설정
    
    # 우선순위 큐 사용 (다익스트라 알고리즘)
    queue = [(0, 0, 0)]  # (비용, x좌표, y좌표)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동

    while queue:
        cost, x, y = heapq.heappop(queue)

        # 현재 위치의 비용이 기존 기록된 비용보다 크다면 무시
        if cost > recovery_cost[x][y]:
            continue

        # 상하좌우 인접한 칸 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + grid[nx][ny]
                # 더 적은 비용으로 도달할 수 있으면 갱신
                if new_cost < recovery_cost[nx][ny]:
                    recovery_cost[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))
                    
    return recovery_cost[n - 1][n - 1]  # 우측 하단까지의 최소 복구 비용

# 테스트 예제
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    result = min_recovery_cost(grid)
    print(f"#{test_case} {result}")