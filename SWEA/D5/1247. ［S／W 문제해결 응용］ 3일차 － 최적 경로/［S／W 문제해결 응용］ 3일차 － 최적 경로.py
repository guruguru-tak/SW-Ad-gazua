from itertools import permutations

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    # 라인에서 처음 두개 회사 좌표, 집 좌표, N명의 고객 좌표
    company_x, compay_y, home_x, home_y, *line = list(map(int, input().split()))

    reline = []
    for i in range(0, len(line), 2):
        customer_x = line[i]
        customer_y = line[i+1]
        reline.append((customer_x, customer_y))

    # 최소값 찾기위해 맥스 값으로 초기화
    min_result = 10**18


    # 모두 탐색 -> 효율x -> 모두면 순열 뽑기
    # 고객 수 10명 이내이기에
    for perm in permutations(reline):

        # 매 순열 생성 하기에 초기화 값 만들기
        result = 0

        # 먼저 회사에서 첫번째 고객 값 구하기
        result = abs(company_x-perm[0][0]) + abs(compay_y-perm[0][1])

        # 고객 집 전과 현재값 비교해서 결과값에 추가
        for index in range(1, len(perm)):
            # 이 조건문으로 1초 감소
            if result < min_result:
                result += abs(perm[index-1][0] - perm[index][0]) + abs(perm[index-1][1] - perm[index][1])
            else:
                break

        # print(result)
        # 마지막 집이랑 마지막 고객값 더하기
        # 이 조건문으로 1초 감소
        if result < min_result:
            result += abs(perm[-1][0] - home_x) + abs(perm[-1][1] - home_y)
        else:
            continue

        # 그리고 최소값 나올때까지 게속 마지막에 갱신
        min_result = min(min_result, result)

    print(f"#{tc} {min_result}")

