t = 10
for tc in range(1, t+1):
    #입력값, 한 줄로 들어오면 한개만 따로 빼고 뒤에는 리스트로 넣는 방법도 있다
    # n, *line
    line = list(input())

    split_line = []
    for i in range(len(line)):
        if line[i] == " ":
            for s in range(i+1, len(line)):
                split_line.append(line[s])

    # print(split_line)

    #pop 같은 번호 양쪽 팝하고 계속 다시 전부 양쪽에 있는지 체크 돌면서 완탐
    #플래그 세워서 전부 무한 반복 돌다가 탈출
    flag = True
    while flag:
        for i in range(len(split_line)):
            flag = False
            if i + 1 < len(split_line) and split_line[i] == split_line[i+1]:
                flag = True
                split_line.pop(i)
                split_line.pop(i)
                break
                
    print(f"#{tc}", end=" ")
    pwd = ''
    for i in split_line:
        pwd += i
    print(pwd)

