t = int(input())

for tc in range(1,t+1):
    n = int(input())

    line = list(map(int, input().split()))

    sum_tree = sum(line)

    # 1단계 가장 높은 나무의 높이
    max_tree = max(line)

    # 2단계 필요한 값 먼저 정의 -> 각 나무마다 부족한 높이 리스트 지정
    necessary = []
    for tree in line:
        necessary.append(max_tree - tree)

    # print(necessary)

    # 짝수는 1, 2 를 이용해서 정확한 차이값 채울 수 있음

    # 홀수 -> 1과 2가 혼합되어 나무를 키울 수 있음

    # 2로 채울 수 있는 날과 1로 채울 수 있는 날을 나눔
    needed_2 = 0
    needed_1 = 0

    # 3단계 부족한 값으로 처리 가능한 날 계산
    for diff in necessary:
        # 차이를 최대한 2로 먼저 보내고, 나머지를 1인 홀수로 보냄

        # 2로 처리할 수 있는 날 계산
        needed_2 += diff // 2
        # 나머지 1로 처리해야 하는 부분
        needed_1 += diff % 2

    # 4단계 홀수와 짝수 중 최솟 값 가져오기
    minTwoday = min(needed_1, needed_2)

    # 짝수, 홀수 두 날에 걸쳐 키우기에 *2로 일자 맞추기
    result = minTwoday * 2

    # 이틀로 사용했기에 각 최소 사용 카운트를 빼주기
    # 최솟값 만큼 서로 소모, 2틀 사용해서
    needed_2 -= minTwoday
    needed_1 -= minTwoday

    # 5단계 이제 남은 값이 짝수냐 홀수냐 구분
    # 홀수 처리
    if needed_1 > 0:
        # 홀수 날만 사용
        # 따라서 *2 => 1더하고, 아무것도 안하고
        # 마지막날은 1만 더하면되기에 -1로 홀수 날만 계산(아무것도 안하는걸 뺌)
        # ex) needed_1 = 3 이면 2*3 - 1 = 5일
        result += needed_1 * 2 - 1

    # 짝수 처리
    else:
        # 짝수 작업은 작업day * 2 환산
        day = needed_2 * 2
        # 짝수는 3일 단위로 묶어 처리
        # 짝수는 홀수+짝수 조합도 처리 가능함 (1+2)

        # day % 3 == 0 => 남은 작업량 없음
        if day % 3 == 0: # -> 3일로 딱 떨어진 경우
            # 3일 단위로 묶어 최적화 처리
            # ex) needed_2 = 3 이면 day = 3*2 = 6
            # 6 // 3 = 2
            # 총 일수 = 2 * 2 = 4일
            # 6을 기르기 위해 1 + 2 + 1 + 2 -> 4일 소요
            result += day // 3 * 2

        # day % 3 != 0 => 남은 작업량이 있어어, 추가적인 이 필요
        else: # -> 3일로 안떨어진 경우
            # (day % 3) -> 남은 작업량 계산
            # ex) needed_2 = 4 이면 day = 4*2 = 8
            # 8 // 3 = 2    , 8 % 3 = 2
            # 총 일수 = 2 * 2 + 2 = 6일
            # 8을 기르기 위해 1 + 2 + 1 + 2 + x + 2 -> 6일 소요
            # 5일차는 1이기에 2를 올리려면 3일 사용하면 비효율
            # 5일차 아무것도 하지 않고 6일차 일하느게 효율
            result += (day // 3 * 2) + (day % 3)

    # 정답 보장되는 이유
    # 번갈아 작업하는 것이 가장 효율적
    # 홀수 날과 짝수 날의 작업을 각각 남은 작업량에 따라 정확히 처리
    print(f"#{tc} {result}")