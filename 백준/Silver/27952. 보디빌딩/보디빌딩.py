def max_routines(n, x, a, b):
    current_weight = 0  # 초기 몸무게

    # 매일 몸무게 증가
    for i in range(n):
        current_weight += b[i]
        if current_weight < a[i]:  # 하한을 만족하지 못하면 즉시 종료
            return -1

    # 마지막 날 기준으로 최대 루틴 계산
    max_routines = (current_weight - a[-1]) // x
    return max_routines


# 입력 처리
n, x = map(int, input().split())  # 첫 줄: n, x
a = list(map(int, input().split()))  # 두 번째 줄: A 리스트
b = list(map(int, input().split()))  # 세 번째 줄: B 리스트

# 결과 출력
print(max_routines(n, x, a, b))
