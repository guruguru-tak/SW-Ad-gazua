t = int(input())
for tc in range(1, t+1):
    d, h, m = map(int, input().split())
    
    # 소개팅 약속 날
    date_d = 11
    date_h = 11
    date_m = 11
    
    # 변환 숫자
    x_h = 24
    x_m = 60

    # 분 단위 변환 수식
    date_min = date_m * x_h * x_m + date_h * x_m + date_m
    comp_min = d * x_h * x_m + h * x_m + m

    # 비교할 분변환 시간이 현재 분변환 시간보다 작으면
    if date_min > comp_min:
        print(f"#{tc} {-1}")
    else:
        # 비교할 분변환 시간이 현재 분변환 시간보다 크면
        print(f"#{tc} {comp_min-date_min}")

