from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    # n 개의 자연수 수열 입력
    n_list = list(map(int , input().split()))

    result = 0
    # 선택할 자연수의 개수를 1개부터 n개까지 전부 탐색
    for i in range(1, n+1):
        #  자연수를 한 번씩만 사용할 수 있으므로, 중복을 허용하지 않는 조합
        # combinations을 사용하여 중복되지 않는 i개의 자연수 조합 생성
        for cp in combinations(n_list, i):
            if k == sum(cp):
                result += 1

    print(f"#{tc} {result}")
