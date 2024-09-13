t = int(input())
for tc in range(1,t+1):
    make_line = list(input().strip())

    reset = []
    for _ in range(len(make_line)):
        reset.append('0')

    # 최소 수정 횟수
    cnt = 0
    # if 문 조건 탈출하면 똑같은 조건으로 만들고자하는거랑 초기화값에서 변경되는거랑 같으면 종료
    while make_line != reset:
        # 처음 0이면 최소로 하기위해 flag 로 초기화 0은 건들지 마라
        # 처음 1이면 최소로 하기위해 flag 로 초기화 1은 건들지 마라
        flag_0 = False
        flag_1 = False
        for i in range(len(make_line)):
            # 만들고자하는거랑 초기화값에서 변경되는거랑 다르면 작업해라
            if make_line[i] == '1' and not flag_1 and make_line != reset:
                # 전체 바꾸는 for 문 전에 cnt + 1 임
                cnt += 1
                # 1로 뒤에 다 덮었기에 1은 작업하지 말고 이제부터 0 덮는거 작동해라
                flag_0 = True
                flag_1 = True
                for j in range(i, len(reset)):
                    reset[j] = '1'


            # 만들고자하는거랑 초기화값에서 변경되는거랑 다르면 작업해라
            elif make_line[i] == '0' and flag_0 and make_line != reset:
                # 전체 바꾸는 for 문 전에 cnt + 1 임
                cnt += 1
                # 뒤에 0 다시 오면 0은 작업하지말고, 1로 가라
                flag_0 = False
                flag_1 = False
                for j in range(i, len(reset)):
                    reset[j] = '0'

    print(f"#{tc} {cnt}")