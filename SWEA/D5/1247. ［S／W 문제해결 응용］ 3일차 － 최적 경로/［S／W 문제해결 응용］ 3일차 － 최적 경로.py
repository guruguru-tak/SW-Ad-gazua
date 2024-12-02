from itertools import permutations

# 20초
# 효율적으로 찾는 것이 목적이 아님
# 고객 수 20 -> 완전 탐색 가능
# 고객 집 한 번만 들려야 한다. -> 조합

t = int(input())
for tc in range(1, t+1):
    # 고객 입력
    n = int(input())

    # 회사, 집, 고객 좌표 입력
    company_x, company_y, home_x, home_y, *line = list(map(int, input().split()))

    result = 0

    # (y ,x) 넣어서 다시 리스트 만들기
    customer = []
    for i in range(1, len(line), 2):
        customer.append((line[i-1], line[i]))

    # print(customer)

    # 최소 경우 찾기 위해 10의 18승 지정
    min_result = 10**18

    for perm in permutations(customer):
        result = 0
        # 먼저 회사와 제일 처음 고객 집 좌표로 초기 값 넣어주기
        result = abs(company_x - perm[0][0]) + abs(company_y - perm[0][1])
        # print(result)

        # y, x 두개 뽑기 위해 for 문 repeat 범위 2로 지정
        for index in range(1, len(perm)):
            if result < min_result:
                # 고객들간 경우 계산
                customer_x = perm[index][0]
                customer_y = perm[index][1]

                result += abs(perm[index-1][0] - customer_x) + abs(perm[index-1][1] - customer_y)
            else:
                break

        # 마지막 집과 집 거리 계산
        result += abs(perm[-1][0] - home_x) + abs(perm[-1][1] - home_y)

        # 최솟 값 갱신
        min_result = min(min_result, result)

    print(f"#{tc} {min_result}")