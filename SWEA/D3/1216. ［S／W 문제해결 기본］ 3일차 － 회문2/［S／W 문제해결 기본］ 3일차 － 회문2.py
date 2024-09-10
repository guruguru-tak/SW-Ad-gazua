t = 10
for tc in range(1, t+1):
    test = int(input())
    n = 100

    grid = [list(map(str, input().strip())) for _ in range(n)]

    max_cnt = 0

    #홀수 일때
    for y in range(n):
        for x in range(n):
            # 첫 번째 1길이 회문 A 한자리 계산
            cnt = 1
            for dist in range(1, n//2):
                # 첫 번째 1길이 회문 0 번지 == 0 번지 이기에 1 추가
                if 0 <= x - dist < n and 0 <= x + dist < n:
                    if grid[y][x-dist] == grid[y][x+dist]:
                        #양쪽 2개씩 추가 됨
                        cnt += 2
                    else:
                        break
                else:
                    break

            max_cnt = max(max_cnt, cnt)

    for y in range(n):
        for x in range(n):
            # 첫 번째 1길이 회문 A 한자리 계산
            cnt = 1
            for dist in range(1, n//2):
                if 0 <= x - dist < n and 0 <= x + dist < n:
                    if grid[x-dist][y] == grid[x+dist][y]:
                        # 양쪽 2개씩 추가 됨
                        cnt += 2
                    else:
                        break
                else:
                    break
            max_cnt = max(max_cnt, cnt)


    # 짝수 일 때
    for y in range(n):
        for x in range(n):
            #짝수는 cnt 2개 합쳐야 2부터 시작
            cnt = 0
            for dist in range(n // 2):
                # 짝수는 어떻게?
                if 0 <= x - dist < n and 0 <= x + dist + 1 < n:
                    if grid[y][x-dist] == grid[y][x + dist + 1]:
                        cnt += 2
                    else:
                        break
                else:
                    break

            max_cnt = max(max_cnt, cnt)

    for y in range(n):
        for x in range(n):
            #짝수는 cnt 2개 합쳐야 2부터 시작
            cnt = 0
            for dist in range(n // 2):
                if 0 <= x - dist < n and 0 <= x + dist + 1 < n:
                    if grid[x - dist][y] == grid[x + dist + 1][y]:
                        cnt += 2
                    else:
                        break
                else:
                    break
            max_cnt = max(max_cnt, cnt)

    print(f"#{test} {max_cnt}")
