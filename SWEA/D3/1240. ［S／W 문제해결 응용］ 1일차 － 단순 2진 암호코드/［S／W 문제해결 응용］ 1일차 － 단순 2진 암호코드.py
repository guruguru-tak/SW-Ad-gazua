# 7비트 코드 수 딕셔너리 지정
code_dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    code = [list(map(str, input().strip())) for _ in range(n)]

    size = 56
    decode_List = [[] for _ in range(size)]

    flag = False
    check = 55
    for y in range(n):
        for x in range(m-1, -1, -1):
            # 코드 뒤에서부터 읽으면 앞자리 찾을 수 있음
            if code[y][x] == '1' and not flag:
            # 바코드이기에 위 한줄만 읽어도 추출 가능
                flag = True
                for i in range(0, size):
                    # 코드 제일마지막 55번지부터 시작이기에
                    # 0번지부터 확인하게 nx 지정
                    nx = (x+1) - (56-i)
                    decode_List[i].append(code[y][nx])

    # 추출한 분해 코드를 7개씩 나누기
    di = 7
    result = []
    for i in range(0, len(decode_List), di):
        # 초기화 위해 선언
        codeSum = ''
        for j in range(0, di):
            # *로 리스트값을 단순 문자열로 꺼내기
            codeSum += str(*decode_List[i+j])
        # 나눈 코드를 결과 리스트에 저장
        result.append(codeSum)

    # code_dic과 비교해서 10진수로 변환하기
    re = []
    for i in result:
        # 코드 딕셔녀리에서 키, 밸류값 꺼내 비교
        for key, val in code_dic.items():
            if i == key:
                re.append(val)
    sum_val = 0
    mul_val = 0
    # 2개의 스텝으로 홀수 짝수값 다 더하기
    for i in range(0, len(re), 2):
        mul_val += re[i]
        sum_val += re[i+1]

    # 공식대로 값 계산
    check_Sum = mul_val*3 + sum_val
    # 10의 배수면 코드 각 자리 수 출력
    if check_Sum % 10 == 0:
        print(f"#{tc} {mul_val + sum_val}")
    # 아니면 0 출력
    else:
        print(f"#{tc} {0}")

