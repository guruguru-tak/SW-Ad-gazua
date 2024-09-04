t = int(input())
for tc in range(1, t +1):

    all_unzip = ""
    for _ in range(int(input())):
        alpha, repeat = map(str, input().split())
        #문자열 곱해서 일단 전부 출력
        all_unzip += alpha*int(repeat)


    #10단위로 자르기
    print(f"#{tc}")
    #range(start, stop, step)/ i는 매번 10씩 증가 step
    for i in range(0, len(all_unzip), 10):
        #슬라이스 인덱싱
        # i = 슬라이스의 시작 인덱스
        # i+10 = 슬라이스의 끝 인덱스입니다 (끝 인덱스는 포함되지 않음).
        print(all_unzip[i:i+10])