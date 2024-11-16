

from collections import deque, defaultdict

# 입력받기
n = int(input())
fruit = list(map(int, input().split()))

# 투 포인터와 결과를 저장할 변수 초기화
left = 0 #서브리스트 시작 지점 포인터
max_length = 0 #두 종류 이하 과일로 만든 가장 긴 탕후루의 길이 저장
fruit_count = defaultdict(int)  # 각 과일의 개수를 저장할 딕셔너리, 기본 딕셔녀리와 유사하나 키 없는 예외 발생 안함

# 오른쪽 포인터를 이동하며 탐색, 리스트의 시작부터 끌까지 이동하면서, 서브리스트에 포함된 과일 갯수 ruit_count 기록
for right in range(n):
    fruit_count[fruit[right]] += 1  # 현재 과일의 개수를 증가시킴

    # 과일 종류가 2개를 초과하면, left 포인터를 오른쪽으로 이동시켜 과일 제거
    while len(fruit_count) > 2:
        fruit_count[fruit[left]] -= 1
        if fruit_count[fruit[left]] == 0:
            del fruit_count[fruit[left]]  # 개수가 0인 과일은 딕셔너리에서 제거
        left += 1  # left 포인터를 오른쪽으로 이동

    # 현재 구간의 길이를 계산하고, left 시작지점, right 끝지점/ 끝지점도 포함 따라서 +1, 최대 길이 갱신
    current_length = right - left + 1
    max_length = max(max_length, current_length)

# 최종적으로 최대 길이를 출력
print(max_length)