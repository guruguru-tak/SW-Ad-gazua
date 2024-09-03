from collections import deque, defaultdict

t = int(input())

#재귀로 change 2부터 -> 0까지 깊이 참색으로 들어간다
def dfs(change):
    global result


    if change == 0:
        result = max(result, int("".join(line_list)))
        #리턴하면 change가 1인 으로 올라가기만 함 // 1개만 올라간다
        return

    #바꿀 값 2 개 선택, 각 깊이마다 for문 2개 있음
    for i in range(len(line_list)):
        for j in range(i+1, len(line_list)):

            #swap / change 1 cnt, ex. visited 처럼 사용, True
            line_list[i], line_list[j] = line_list[j], line_list[i]

            #딕셔너리는 입력값으로 str, int 밖에 안됨, list -> str
            temp = "".join(line_list)
            #재귀 호출, 깊이 내려가기 (-1) / change == 0이면 return으로 여기부터 시작
            #그 위에서 한 단계 아래 탐색 할 예정
            if (temp, change-1) not in dic:
                #딕셔너리에 키값으로 숫자리스트와, 내려갈 깊이단계가 없으면 넣고
                #{(line_list, change-1):1} => 중복제거용으로 묶임
                dic[(temp, change-1)] = 1
                # 묶고 중복이 없을 때만 재귀 호출
                dfs(change-1)
            # 바꾼 값 다시 바꾸기, visited 다시 False 로 변환
            # 최종 가지 다 탐색하면, 외부for문이 증가, 내부 for문 종료 // 깊이 단계는 아님
            line_list[i], line_list[j] = line_list[j], line_list[i]


for tc in range(1, t + 1):
    result = 0
    line, change = input().split()
    line_list = list(line)
    #빈 공간 딕셔너리 에러 방지용 디폴트 딕
    dic = defaultdict()

    #재귀함수 호출, change 숫자로 단계 빼기위해 type-casting
    dfs(int(change))

    print(f"#{tc} {result}")