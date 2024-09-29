from itertools import permutations

t = int(input())
for tc in range(1, t+1):
    customer = int(input())
    company_y, company_x, home_y, home_x, *customer_List = map(int, input().split())

    comp_list = []
    # 출발지부터 다음 지점 y, x 좌표 뺀 다음 절대값의 합으로 비교해서 제일 최단 길로 가야함
    # y, x 2차원 배열 만들기
    for i in range(customer):
        y = customer_List.pop(0)
        x = customer_List.pop(0)
        comp_list.append([y, x])

    # 최단 경로를 계산할 변수
    min_distance = 10**18

    # 고객 방문 순서를 순열로 모두 탐색
    for perm in permutations(comp_list):
        # 먼저 회사에서 시작해서 고객 집까지 비교
        temp_y, temp_x = company_y, company_x
        total_distance = 0

        for y, x in perm:
            total_distance += (abs(y - temp_y) + abs(x - temp_x))
            temp_y, temp_x = y, x

        # 마지막으로 고객집에서 본인집까지 집 계산
        total_distance += (abs(home_y - temp_y) + abs(home_x - temp_x))

        # 가장 짧은 경로 저장
        min_distance = min(min_distance, total_distance)

    print(f"#{tc} {min_distance}")