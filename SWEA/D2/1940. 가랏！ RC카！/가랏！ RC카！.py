t = int(input())
for tc in range(1, t+1):
    command = int(input())

    now_accel = 0
    move = 0
    for _ in range(command):
        line = list(map(int, input().split()))
        if len(line) == 2:
            cmd, accel = line[0], line[1]
            if cmd == 1:
                now_accel += accel
                move += now_accel
            else:
                if now_accel < accel:
                    now_accel = 0
                    move += now_accel
                else:
                    now_accel -= accel
                    move += now_accel
        else:# 0이면 유지
            move += now_accel

    print(f"#{tc} {move}")