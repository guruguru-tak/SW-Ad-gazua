t = 10
for tc in range(1, t+1):
    dump_cnt = int(input())
    line = list(map(int, input().split()))

    #덤프 횟수 0까지 계속 반복
    while dump_cnt != 0:
        
        # 비교할 가장 큰 수, 작은 수 구하기
        high = max(line)
        low = min(line)

        # 매 번 가장 큰 수 찾기 위해 계속 탐색
        # 덤프 행위 한 번하면 카운트 내리기
        dump_cnt -= 1
        for x in range(len(line)):
            # 가장 큰 수의 인덱스 얻기
            if high == line[x]:
                # 가장 큰 수에서 1 빼고 다시 넣기
                line[x] = high - 1
                # 행위 종료
                break

        for x in range(len(line)):
            # 가장 작은 수의 인덱스 얻기
            if low == line[x]:
                # 가장 작은 수에서 1 추가하고 다시 넣기
                line[x] = low + 1
                # 행위 종료
                break

    print(f"#{tc} {max(line) - min(line)}")