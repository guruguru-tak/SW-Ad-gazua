t = int(input())
for tc in range(1, t+1):
    n = int(input())

    di = [2, 3, 5, 7, 11]

    result = [0]*5
    j = 0
    for i in di:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
            result[j] = cnt
        j += 1
    # * 은 리스트 에서 대괄호([, ]) 와 콤마(,) 벗겨주는 용도
    print(f'#{tc}',*result)