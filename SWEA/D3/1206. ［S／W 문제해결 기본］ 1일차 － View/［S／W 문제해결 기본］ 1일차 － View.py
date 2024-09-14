
t = 10
for tc in range(1, t+1):
    _ = input()
    line = list(map(int, input().split()))

    # 조망권 갯수
    cnt = 0
    # 범위 잡기
    for x in range(2, len(line)-2):
        max_line = 0
        # 가장 큰 조망권 방해 빌딩 찾기
        max_line = max(max_line, line[x-2], line[x-1], line[x+1], line[x+2])
        if line[x] > max_line:
            cnt += line[x] - max_line
        else:
            pass

    print(f"#{tc} {cnt}")



