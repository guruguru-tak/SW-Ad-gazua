t = int(input())
for tc in range(1,t+1):
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]

    # print(grid)

    # row 시작하고 양쪽+1 씩 증가하다 col 중간 이후부턴 양쪽 -1 감소
    # 양쪽 길이 인덱스 잡아 줄 size값 
    size = -1

    result = 0
    for y in range(n):
        # 결국 n 은 홀수 이고, n 의 몫이 나오는 인덱스가 모든 row 합하는 경우
        # n의 몫 전까진 size += 1 / n 몫 이후부터 size -= 1 
        start_size_idx = n//2
        check_point = n//2
        # 좌 우 체크할 범위 사이즈 증가
        # n=1 경우 위해 = 등호와, size -1로 시작해 0부터 셈하도록 시작
        # 비교대상은 y 인덱스 값
        if check_point >= y:
            size += 1
        else:
            size -= 1
        # x좌표 범위를 정중앙으로 잡고 좌 우 양쪽 size 차 만큼 x 전부 반복
        # 마지막은 포함 안되기에 start_size_idx+size+1
        for x in range(start_size_idx-size, start_size_idx+size+1):
            # print(start_size_idx-size, start_size_idx+size+1)
            # print(size)
            # print(grid[y][x])
            result += grid[y][x]

    print(f"#{tc} {result}")

