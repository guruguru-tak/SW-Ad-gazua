import sys

# sys.stdin = open("input.txt", "r", encoding='utf-8')

from bisect import bisect_left, bisect_right


# line 값, 체크할 숫자가 인자
# 특정 숫자가 배열에서 몇 개 있는지 찾기
def binary_Search(array, target):
    # array에서 target이 처음 등장하는 위치를 반환
    left_index = bisect_left(array, target)
    
    # array에서 target이 마지막으로 등장한 위치의 '다음 인덱스(해당 숫자 아닌 인덱스'를 반환
    # target보다 큰 값이 처음 등장하는 위치를 반환
    
    # 만약 마지막번지 수가 target 이라면
    # 배열에서 더 이상 큰 수 없기에 배열길이 반환함
    right_index = bisect_right(array, target)
    
    # 정렬한 상태에서 제일 마지막 target 다음 순번인 right_index에서
    # 처음 등장한 left_index 를 빼면
    # array = [1, 2, 2, 2, 3]
    # target = 2 면 right_index = 4, left_index = 1
    # 따라서 4-1 = 3개
    return right_index - left_index


input = sys.stdin.readline

n = int(input().strip())
line = list(map(int, input().strip().split()))

m = int(input().strip())
check = list(map(int, input().strip().split()))

# 이분탐색 위해 오름차순 정렬
line.sort()

result = []
for number in check:
    count = binary_Search(line, number)
    result.append(count)

print(*result)




