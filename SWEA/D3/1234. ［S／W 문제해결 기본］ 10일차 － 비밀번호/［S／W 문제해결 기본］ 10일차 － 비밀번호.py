t = 10
for tc in range(1, t+1):
    line = list(map(str, input().strip()))

    # 문자열 입력 숫자만 받기
    int_Line = []
    for i in range(len(line)):
        if line[i] == " ":
            for j in range(i+1, len(line)):
                int_Line.append(int(line[j]))

    # 인접 숫자만 제거 위해 while문 한 번 돌면
    # for 문 범위까진 한 번 반복함
    # break 걸면 for 문 종료 -> while 조건 다시 체크
    flag = True
    while flag:
        for i in range(1, len(int_Line)):
            # 일치하는 것 한 개 찾으면, flag 다시 True 로 바꾸고
            # for 문 종료시키고 다시 돌기
            if int_Line[i-1] == int_Line[i]:
                # pop하면 인덱스 범위 달라짐
                int_Line.pop(i-1)
                # 다시 1단계 줄어든 인덱스 pop
                int_Line.pop(i-1)
                flag = True
                break
            else:
                # 일치하는게 없으면 for 문 종료 후
                # while 문 탈출 조건
                flag = False

    print(f"#{tc}", end=" ")
    for i in int_Line:
        print(i, end="")
    print()