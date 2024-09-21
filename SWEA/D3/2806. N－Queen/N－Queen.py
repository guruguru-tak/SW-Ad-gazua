t = int(input())


# 이 함수는 현재 행에 퀸 배치시, 이전에 배치한 퀸들과 충동하지 않은지 체킹
def checking(row):
    for i in range(row):
        # 같은 열에 퀸이 있는지 확인하거나 대각선 있는지 확인
        # 대각선 규칙 => 2 개의 비교하과 하는 퀸이 있으면
        # 퀸이 (1, 2) (3, 4) -> 절대 값으로 3-1 == 4-2 같으면 서로 같은 대각선에 존재
        # 만약 3-1 != 4-1 이면 대각선이 아님
        if col[row] == col[i] or row - i == abs(col[row] - col[i]):
            # 퀸이 같은 대각선 또는 열에 존재한다면 탐색 중지
            return False
    # 충돌 없음 반환
    return True


def dfs(row):
    global result
    # 모든 각 행에 퀸을 배치한 경우
    if row == n:
        # 안 겹치게 모든 퀸 배치 경우만 result + 1
        result += 1
    else:
        # 현재 행의 모든 열 탐색
        # row 행의 어느 열 선택해서
        for c in range(n):
            # 퀸을 현재 열에 배치
            col[row] = c

            # 배치 유효한지 다시 체크
            # (Backtracking) 더 탐색할지 결정
            if checking(row):
                # 다음 행 이동 / 재귀
                # True 값 받으면
                # 현재 행(row)에 퀸을 배치한 위치가 유효
                # -> 따라서 다음 퀸 배치(dfs(row+1)) 시작

                # False 값 받으면
                # 현재 행(row)에 퀸을 배치한 위치가 유효하지 않음
                # -> 따라서 dfs(row+1) 작동 안하고,
                # 다음 열 루프(c +1) 시작
                dfs(row+1)

for tc in range(1, t+1):
    n = int(input())
    # 백트래킹(재귀)으로 탐색
    # DFS에서 체스판 깊이가 행,

    # 먼저 퀸 위치 저장할 열 생성
    col = [-1]*n
    result = 0

    # 첫 번째 행부서 체크
    dfs(0)

    print(f"#{tc} {result}")

