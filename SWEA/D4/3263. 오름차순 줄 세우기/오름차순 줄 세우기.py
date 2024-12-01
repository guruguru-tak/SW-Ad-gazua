t = int(input())

for tc in range(1, t+1):
    n = int(input())

    line = list(map(int, input().split()))

    # 현재 수가 지금인덱스 +1 과 동일하면 넘기면 됨
    # 아니라면 지금 왼쪽 끝이나 오른쪽 끝이 내 인덱스 번호면 옮기기
    # -> 이 방식은 On**2 -> 비효율

    # 그리디 방식
    # 번호 순서에 따른 인덱스 배열을 먼저 계산
    # 현재 배열의 번호가 원래 위치에서 몇 번째인지 알 수 있도록 변환
    # 입력 5 2 4 1 3은 B=[3,1,4,2,0]로 변환
    # B에서 인덱스가 연속적으로 증가하는 부분을 최장 증가 부분 수열(LIS)으로 간주
    # 즉 실제 배열 정보가 아닌, 위치 정보로 증가 여부 판단

    # 위치 정보 저장 배열 생성
    location = [0] * n

    for i in range(n):
        # 처음 입력 배열 값에서 -1 을 빼서 0번지 부터 위치 차이 값 저장
        location[line[i] - 1] = i

    # 해당 숫자의 인덱스 위치 번호가 저장됨
    # 원래 리스트에서 5는 0번지 위치, 1은 3번지 위치
    # print(location)

    max_count = 0
    count = 1

    # 비교 위해 1부터 n미만까지 범위
    for i in range(1, n):
        # 연속 증가 부분 인덱스 수열 구하기
        # i 보다 그 다음 값이 더 크면 연속 증가 부분 수열 길이 증가
        if location[i-1] < location[i]:
            count += 1

            # 현재 연속 증가 부분 수열이 최대보다 크면
            if max_count < count:
                # 최대 값 갱신해주기
                max_count = count

        # 연속 증가 부분 수열 끊기면 다시 1로 초기화
        else:
            count = 1

    # 최종 값은 전체 길이에서 연속 증가 부분수열 최대값 뺀 것
    # 그러면 최소 교환 행위 보장됨
    result = n - max_count
    print(f"#{tc} {result}")