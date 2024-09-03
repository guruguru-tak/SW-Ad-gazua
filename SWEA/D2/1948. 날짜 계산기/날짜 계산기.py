#문자열 들고 와서. (,)로 분리해서 s에 담고, s를 /로 구분해서 0번지는 달, 1번지는 일수로 저장
month = [list(map(int, s.strip().split("/")))[1] for s in "1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31".split(",")]

# print(month)
t = int(input())
for tc in range(1, t+1):
    m_1, d_1, m_2, d_2 = map(int, input().split())
    result = 0
    if m_2 - m_1 == 0:
        result = (d_2 - d_1 + 1)
    else:
        leng = m_2 - m_1
        #최대 달의 일수 추가
        result += d_2
        # print(result)
        for i in range(1, leng):
            #각 달 일 수 추가 0번지 부터 시작
            result += month[m_2 - i - 1]
            # print(result, m_2- i)

        #마지막 m-1 달 값 더하고, 들어온 일자값 + 1 하기
        result += month[m_1-1] - d_1 + 1
        # print(result)
    print(f"#{tc} {result}")