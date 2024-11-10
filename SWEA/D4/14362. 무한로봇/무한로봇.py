for tc in range(1, int(input()) + 1):
    # 명령 문자열을 입력
    s = input()
    # 명령 문자열을 4번 반복
    s *= 4
    # 초기 위치와 방향을 설정합니다.
    x, y = 0, 0  # 위치
    dx, dy = 1, 0  # 방향 벡터 (동쪽)

    # 이동 중 최대 거리를 저장할 변수
    max_dist_sq = 0
    # 명령 문자열을 순회하면서 이동
    for c in s:
        if c == "S":
            x += dx
            y += dy
            dist_sq = x ** 2 + y ** 2
            max_dist_sq = max(max_dist_sq, dist_sq)
        elif c == "L":
            dx, dy = -dy, dx
        elif c == "R":
            dx, dy = dy, -dx

    # 4번의 반복 후에 로봇이 원점으로 돌아왔는지 확인
    if x == 0 and y == 0:
        # 유한한 이동인 경우 최대 거리를 출력
        print(f"#{tc} {max_dist_sq}")
    else:
        # 무한 이동인 경우 oo를 출력
        print(f"#{tc} oo")