def execute_program(grid, R, C):
    from collections import deque

    # 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 초기 상태: (행, 열, 방향, 메모리)
    queue = deque([(0, 0, 0, 0)])
    # 방문 체크 배열
    visited = [[[[False] * 16 for _ in range(4)] for _ in range(C)] for _ in range(R)]

    while queue:
        r, c, d, mem = queue.popleft()

        if visited[r][c][d][mem]:
            continue
        visited[r][c][d][mem] = True

        cmd = grid[r][c]

        if cmd == '@':
            return "YES"
        elif cmd == '>':
            d = 0
        elif cmd == 'v':
            d = 1
        elif cmd == '<':
            d = 2
        elif cmd == '^':
            d = 3
        elif cmd == '_':
            d = 0 if mem == 0 else 2
        elif cmd == '|':
            d = 1 if mem == 0 else 3
        elif cmd == '?':
            for i in range(4):
                nr = (r + dx[i]) % R
                nc = (c + dy[i]) % C
                if not visited[nr][nc][i][mem]:
                    queue.append((nr, nc, i, mem))
            continue
        elif cmd == '+':
            mem = (mem + 1) % 16
        elif cmd == '-':
            mem = (mem - 1) % 16
        elif cmd.isdigit():
            mem = int(cmd)

        nr = (r + dx[d]) % R
        nc = (c + dy[d]) % C

        if not visited[nr][nc][d][mem]:
            queue.append((nr, nc, d, mem))

    return "NO"

# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [input().strip() for _ in range(R)]
    result = execute_program(grid, R, C)
    print(f"#{tc} {result}")