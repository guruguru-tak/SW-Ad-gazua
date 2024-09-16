t = 10
for tc in range(1, t+1):

    _ = input()
    cnt_str = list(input().strip())
    line = list(input().strip())
    # print(len(cnt_str))
    # print(len(line))

    cnt = 0
    for i in range(len(line)):
        # 길이만큼 모든 글자 하나하나 일치하는지 비교 플래그
        flag = 0
        for j in range(len(cnt_str)):
            # 인덱스 범위 초과 막기 위한 벽
            if i + j >= len(line): continue
            # 만약 비교하는 문자열 첫글자와 긴 문자열 첫 글자 같으면 비교
            if cnt_str[j] == line[i+j]:
                # print("true", cnt_str[j], line[i+j])
                flag += 1
            else:
                # print("false", cnt_str[j], line[i + j])
                flag = 0
        if flag == len(cnt_str):
            cnt += 1

    print(f"#{tc} {cnt}")