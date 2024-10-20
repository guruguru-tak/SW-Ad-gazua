import sys
from bisect import bisect_left

# sys.stdin = open("input.txt", "r", encoding='utf-8')

input = sys.stdin.readline

# n 값을 받아서 정수로 변환
n = int(input().strip())
# input().strip() -> 라인 맨 뒤 공백 제거하고 split() 로 스페스이 기준 나누기
line = list(map(int, input().strip().split()))

# m 값을 받아서 정수로 변환
m = int(input().strip())
# m개의 숫자를 1차원 리스트로 읽음
inline_Check = list(map(int, input().strip().split()))

# 이분탐색 위해 오름차순 정렬 필요
line.sort()

# 이분탐색 함수 정의
# line 값, 체크할 숫자가 인자
def binary_search(array, target):
    # bisect_left 함수 사용 -> 정렬된 리스트에서 target의 삽입 위치를 반환
    index = bisect_left(array, target)

    # 종료 조건 선언언
    # 배열 범위 안에 있고, 해당 위치의 값이 target과 같은 경우에만 찾았다고 판단
    if index < len(array) and array[index] == target:
        return 1
    else:
        return 0

for number in inline_Check:
    # inline_Check의 각 값에 대해 line에 존재하는지 이분탐색으로 확인
    print(binary_search(line, number))



