from itertools import combinations
# 중복을 허용하지 않고 순서를 고려하지 않는 부분집합

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    line = list(map(int, input().split()))

    # 경우의 수 담을 변수
    count = 0

    # 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수
    # if sum(i) == k:
    # 중복허용 안함, 서로 다른 원소 한번씩 사용 -> 부분 수열
    for index in range(1, n + 1):
        for i in combinations(line, index):
            sum_i = sum(i)
            if sum_i == k:
                count += 1
                # print(index)
                # print(i)

            # print(sum_i)

    print(f"#{tc} {count}")