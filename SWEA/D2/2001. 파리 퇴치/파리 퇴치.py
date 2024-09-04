t = int(input())
for tc in range(1, t +1):



    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]


    result = 0
    for y in range(n-m+1):
        for x in range(n-m+1):
            fly_sum = 0
            for i in range(m):
                for j in range(m):
                    fly_sum += grid[y+i][x+j]
            result = max(fly_sum, result)

    print(f"#{tc} {result}")



