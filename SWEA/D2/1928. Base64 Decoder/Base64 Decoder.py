t = int(input())

for tc in range(1, t+1):

    list_a = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    for i in range(ord('a'), ord('z')+1):
        list_a.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        list_a.append(chr(i))
    list_a.append(chr(ord('+')))
    list_a.append(chr(ord('/')))
    # print(list_a)

    base64_line = list(input())
    result = ''

    #입력값 base64 리스트의 해당 인덱스 번호 교환 -> 2진수로 변환후 -> 쪼개서 utf-8로 변환
    for i in range(len(base64_line)):

        num = list_a.index(base64_line[i])
        #단순 숫자 더하면 숫자 합 나오기에, str로 받아야 한다.,
        #2진수 값이면 앞에 0b 참조되어 나온다 / 2번째 인덱스부터 시작해서 제거하기
        bin_num = str(bin(num)[2:])
        # print(bin_num)

        #들어오는 숫자가 6비트 수가 되어야 함, 6비트 수 안나오면 0을 계속 추가하여 6자리 맞추기
        while len(bin_num) < 6:
            #앞 자리부터 0 추가
            bin_num = '0' + bin_num

        #2진수 모든 문자열로 저장
        result += bin_num

    answer = ''
    #이진수로 6자리씩 더한 결과값에 // 8 의 몫을 8자리로 나누기
    for j in range(len(result)//8):
        #+8 로 8비트씩 자르기 ',' 는 기본이 base = 10인데 2면, 2진수 값이라는 뜻
        r = int(result[j*8:j*8+8], 2)
        #r은 int 형 아스키 번호
        answer += chr(r)

    print(f"#{tc} {answer}")
