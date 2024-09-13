t = int(input())
for tc in range(1, t+1):
    n, a, b = map(int, input().split())

    # 타일 전부 안쓰는 경우도 있음
    # 모든 경우의 수 [r, c] -> 만들기
    all_RC = []

    # r 경우의 수만 뽑으면 c 나옴
    # 1번 케이스 r 은 가로 세로 나뉘기에 루트 n 보다 클 수 없음
    # sqrt -> n**0.5
    for r in range(1, int(n**0.5)+1):
        c = n//r
        all_RC.append([r, c])

    # r = c 인 경우 찾기
    # 2번 케이스 r로 나오는게 c랑 같은 경우도 게산해야 한다
    for r in range(1, int(n**0.5)+1):
        c = r
        all_RC.append([r, c])

    # print(all_RC)

    min_result = 10**18
    for r, c in all_RC:
        # 수식에서 n = 4, a = 2, b = 2 이면 각 항 0이 됨
        # 0 경우도 계산해야 됨
        temp = ((a * abs(r - c)) + (b * (n - (r * c))))
        if temp >= 0:
            min_result = min(min_result, temp)

    print(f"#{tc} {min_result}")