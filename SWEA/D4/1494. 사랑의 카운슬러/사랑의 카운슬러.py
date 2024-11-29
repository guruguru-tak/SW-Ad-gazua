from itertools import combinations

t = int(input())
for tc in range(1, t+1):

    n = int(input())
    line = []

    for _ in range(n):
        x, y = map(int, input().split())
        line.append((x,y))

    # 최소 벡터 합 크기
    min_V = 10**18

    # 임의의 지렁이 2마리가 있다
    # 최대 20마리 -> 완탐 가능
    result_V = []
    # 전체의 지렁이를 2개의 그룹으로 나눈다 -> 조합 이용
    # 입력 N // 2 로 2등분
    for combi in combinations(line, n // 2):
        group_a_x, group_a_y = 0, 0

        # print(combi)
        # 조합으로 선택된 지렁이를 그룹 A로 간주
        # 나눈 그룹 중 A 의 합 계산
        for x, y in combi:
            group_a_y += y
            group_a_x += x

        # 나머지를 그룹 B로 간주
        # 그룹 B는 (전체 합 - 그룹 A 의 합)
        group_b_x, group_b_y = 0, 0
        # 먼저 전체 합 구하고
        for x, y in line:
            group_b_x += x
            group_b_y += y
        # 전체에서 A 합 빼기
        group_b_x -= group_a_x
        group_b_y -= group_a_y

        # 두 그룹의 좌표 차이를 계산 벡터 합 크기 구하기
        vertor_Sum = (group_b_x - group_a_x) **2 + (group_b_y - group_a_y) **2

        min_V = min(min_V, vertor_Sum)

    print(f"#{tc} {min_V}")

