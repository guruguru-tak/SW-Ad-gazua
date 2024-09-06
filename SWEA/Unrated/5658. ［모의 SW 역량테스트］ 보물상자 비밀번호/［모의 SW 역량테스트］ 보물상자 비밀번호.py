T = int(input())
for tc in range(1, T + 1):
    n_len, idx = map(int, input().split())

    #입력후 반대로 생각해서 하기
    str_arr = list(input().strip())


    #파싱하고자 하는 변수, 몫 정수형 받기
    parsing = n_len // 4

    #중복 입력 제거용 셋 초기화
    result_set = set()
    # print(str_arr)

    # 역방향으로 기본 0번지 뽑아서 먼저 수에 넣기
    # 넣을려면 역 방향 한 수 다 넣기
    # 방향 바꿀때마다 n / 3 으로 파싱해서 4개의 16진수 수 추가 rotate_cnt 만큼 반복
    
    #모든 경우의 수 다 찾아 회전하기에 parsing 번 회전임
    # 모든 경우의 수 해도 되기에 28번 해도 됨
    for i in range(28):
        # temp 사용 전 초기화
        #0번 첫 입력 넣고
        temp_16 = []

        # 파싱을 4의배수로 하기 -> 12/ 4 => 3 으로 파싱
        # 8이면 8/4 => 2 로 파싱
        str_16 = [str_arr[k : k + parsing] for k in range(0, len(str_arr), parsing)]
        # print(str_16)

        for j in range(len(str_16)):
            temp = ""
            for k in range(parsing):
                #문자열 파싱만큼 더하기
                temp += str_16[j][k]
            # print(temp)
            # set에 16진수 -> 10진수 변환 중복제거 추가
            result_set.add(int(temp, 16))
        # print(result_set)

        #뱡향 전환 위해, 역순
        str_arr.reverse()
        #제일 왼쪽 꺼내서
        temp = str_arr.pop(0)
        #오른쪽 넣기
        str_arr.append(temp)
        # 다시 정방향
        str_arr.reverse()


    # 다 넣고 나면 set을 sort하고 1번부터 센 idx 인 10번째 수 뽑기
    #set을 리스트로 변환 후 -> 정렬하기
    list_set = list(result_set)
    list_set.sort(reverse=True)
    # print(list_set)
    print(f"#{tc} {list_set[idx-1]}")
