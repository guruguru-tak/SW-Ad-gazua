t = 10
for tc in range(1, t+1):
    # 테케 번호 무작위로 주기에 tc로 뽑으면 오류 남
    testcase = int(input())
    n = 100
    grid = [list(input().strip()) for _ in range(n)]

    # 최대 길이 찾기
    max_Result =0

    # 홀수 기준 최대길이 먼저 찾기
    # 홀수 행 체크
    for y in range(n):
        for x in range(n):
            # 기본 자기 위치 1
            cnt = 1
            # 회문 인덱스 2배씩 증가기에 전체 길이의 // 2 가 범위
            for r in range(1, n//2):
                # 벽세우기
                if x - r < 0 or x + r >= n: break
                # 현재 인덱스 기준 좌, 우 계속 + 1 씩 해서 비교
                if grid[y][x+r] == grid[y][x-r]:
                    cnt += 2
                else:
                    break
            # 최대값 비교, 비교 대상 적어야 퍼포먼스 올릴 수 있다
            max_Result = max(max_Result, cnt)

    # 홀수 열 체크
    for y in range(n):
        for x in range(n):
            # 기본 자기 위치 1
            cnt = 1
            for r in range(1, n//2):
                if x - r < 0 or x + r >= n: break
                # 열
                if grid[x+r][y] == grid[x-r][y]:
                    cnt += 2
                else:
                    break
            max_Result = max(max_Result, cnt)

    # 짝수 기준 최대길이 찾기
    # 홀수 행 체크
    for y in range(n):
        for x in range(n):
            # 기본 자기 위치 0
            cnt = 0
            # 회문 인덱스 2배씩 증가기에 전체 길이의 // 2 가 범위
            for r in range(1, n // 2):
                if x - r + 1< 0 or x + r >= n: break
                # 행
                # 현재 인덱스와 1칸 바로 옆에 2개씩 비교
                if grid[y][x + r] == grid[y][x - r + 1]:
                    cnt += 2
                else:
                    break
            max_Result = max(max_Result, cnt)

    # 홀수 열 체크
    for y in range(n):
        for x in range(n):
            # 기본 자기 위치 0
            cnt = 0
            for r in range(1, n // 2):
                if x - r  + 1< 0 or x + r >= n: break
                # 열
                if grid[x + r][y] == grid[x - r + 1][y]:
                    cnt += 2
                else:
                    break
            max_Result = max(max_Result, cnt)

    print(f"#{testcase} {max_Result}")