t = 10
for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]


    cnt = 0
    for x in range(n):
        # n극 s극 만났는지 flag 매 row마다 fasle 디폴트
        flag = False
        for y in range(n):
            # n극 이면 1이고,
            # 1 인식했다는 flag = True 설정
            # 1 -> 1 -> 2 라도 결국 1 -> 2 면 만난 것
            # 2 -> 1 이 경우만 피하면 됨
            if grid[y][x] == 1 and not flag:
                flag = True
            # 1 인식했고, 그 사이에 2만나면 cnt 증가
            # 다시 flag = false
            elif grid[y][x] == 2 and flag:
                cnt += 1
                flag = False
            else:
                pass

    print(f"#{tc} {cnt}")

