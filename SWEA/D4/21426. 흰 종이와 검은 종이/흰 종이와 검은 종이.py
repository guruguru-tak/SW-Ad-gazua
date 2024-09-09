for testcase in range(int(input())):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))
    x5, y5, x6, y6 = list(map(int, input().split()))

    # 첫 번째 블랙 종이가 흰 종이를 완전히 덮는지 확인
    if x3 <= x1 and x4 >= x2 and y3 <= y1 and y4 >= y2:
        print("NO")
        continue

    # 첫 번째 블랙 종이가 부분적으로 덮는 경우 좌표 업데이트
    if x3 <= x1 and x4 >= x2:
        if y3 <= y1 and y4 >= y1 and y4 <= y2:
            y1 = y4  # 위쪽을 덮는 경우
        if y3 >= y1 and y3 <= y2 and y4 >= y2:
            y2 = y3  # 아래쪽을 덮는 경우
    if y3 <= y1 and y4 >= y2:
        if x3 <= x1 and x4 >= x1 and x4 <= x2:
            x1 = x4  # 왼쪽을 덮는 경우
        if x3 >= x1 and x3 <= x2 and x4 >= x2:
            x2 = x3  # 오른쪽을 덮는 경우

    # 두 번째 블랙 종이가 흰 종이를 완전히 덮는지 확인
    if x5 <= x1 and x6 >= x2 and y5 <= y1 and y6 >= y2:
        print("NO")
    else:
        print("YES")
